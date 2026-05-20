"""Mocked tests for CoolAutomationClient.subscribe_unit_updates.

No live API: aiohttp.ClientSession.ws_connect is patched to return a fake
WS that delivers a scripted sequence of messages.
"""
from __future__ import annotations

import asyncio
import json
import unittest
from contextlib import asynccontextmanager
from unittest.mock import MagicMock, patch

import aiohttp

from cool_open_client.cool_automation_client import CoolAutomationClient
from cool_open_client.utils.singleton import SingletonMeta
from cool_open_client.ws_events import Reconnected, UnitUpdate


def _make_text_msg(payload: dict) -> MagicMock:
    msg = MagicMock()
    msg.type = aiohttp.WSMsgType.TEXT
    msg.data = json.dumps(payload)
    return msg


class _FakeWs:
    """Stand-in for aiohttp.ClientWebSocketResponse.

    Scripted: returns each message from `incoming` in turn; raises
    `terminate_with` after the script is exhausted (defaults to a closed
    connection error so the library treats it as a disconnect).
    """

    def __init__(self, incoming, terminate_with=None):
        self._incoming = list(incoming)
        self._terminate = terminate_with or ConnectionResetError("script done")
        self.sent = []
        self.closed = False

    def __aiter__(self):
        return self

    async def __anext__(self):
        if not self._incoming:
            raise self._terminate
        return self._incoming.pop(0)

    async def send_json(self, payload):
        self.sent.append(payload)

    async def close(self):
        self.closed = True


def _make_unit_update_payload(unit_id: str, setpoint: int = 22) -> dict:
    return {
        "name": "UPDATE_UNIT",
        "data": {
            "unitId": unit_id,
            "ambientTemperature": 23,
            "fan": 1,
            "filter": False,
            "operationMode": 2,
            "operationStatus": 1,
            "setpoint": setpoint,
            "swing": 0,
        },
    }


class SubscribeUnitUpdatesTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        SingletonMeta._instances.pop(CoolAutomationClient, None)
        self.client = CoolAutomationClient.__new__(CoolAutomationClient)
        self.client.token = "test-token"
        self.client.logger = MagicMock()
        # _transform_message reads these dictionaries; stub them to identity.
        self.client.fan_modes = MagicMock(get=lambda v: v)
        self.client.operation_modes = MagicMock(get=lambda v: v)
        self.client.operation_statuses = MagicMock(get=lambda v: v)
        self.client.swing_modes = MagicMock(get=lambda v: v)
        # subscribe_unit_updates accesses the REST client's ssl_context.
        self.client.api_client = MagicMock()
        self.client.api_client.rest_client = MagicMock()
        self.client.api_client.rest_client.ssl_context = None

    async def asyncTearDown(self):
        SingletonMeta._instances.pop(CoolAutomationClient, None)

    @staticmethod
    def _patch_ws_connect(fake_wss, fake_session_holder=None):
        """Return a patch that swaps aiohttp.ClientSession with a stub
        whose ws_connect yields each `fake_wss` in order."""

        class _Sess:
            def __init__(self):
                self._wss = list(fake_wss)
                self.closed = False

            def ws_connect(self, *a, **kw):
                ws = self._wss.pop(0)

                @asynccontextmanager
                async def _cm():
                    yield ws

                return _cm()

            async def close(self):
                self.closed = True

        sess = _Sess()
        if fake_session_holder is not None:
            fake_session_holder.append(sess)
        return patch("aiohttp.ClientSession", return_value=sess)

    async def test_yields_unit_update_per_update_unit_message(self):
        fake = _FakeWs(
            incoming=[
                _make_text_msg(_make_unit_update_payload("unit-A", setpoint=22)),
                _make_text_msg({"name": "UPDATE_SENSOR", "data": {}}),
                _make_text_msg(_make_unit_update_payload("unit-B", setpoint=20)),
            ],
            terminate_with=asyncio.CancelledError(),
        )
        with self._patch_ws_connect([fake]):
            events = []
            try:
                async for ev in self.client.subscribe_unit_updates():
                    events.append(ev)
            except asyncio.CancelledError:
                pass

        unit_updates = [e for e in events if isinstance(e, UnitUpdate)]
        self.assertEqual(len(unit_updates), 2)
        self.assertEqual(unit_updates[0].message.unit_id, "unit-A")
        self.assertEqual(unit_updates[1].message.unit_id, "unit-B")
        # Auth handshake sent on connect.
        self.assertEqual(fake.sent[0]["type"], "authenticate")
        self.assertEqual(fake.sent[0]["content"]["token"], "test-token")

    async def test_emits_reconnected_after_drop(self):
        ws1 = _FakeWs(
            incoming=[_make_text_msg(_make_unit_update_payload("unit-A"))],
            terminate_with=ConnectionResetError("drop"),
        )
        ws2 = _FakeWs(
            incoming=[_make_text_msg(_make_unit_update_payload("unit-B"))],
            terminate_with=asyncio.CancelledError(),
        )

        # Patch asyncio.sleep so backoff is instant in the test.
        async def _instant_sleep(_):
            return

        with self._patch_ws_connect([ws1, ws2]), \
             patch("cool_open_client.cool_automation_client.asyncio.sleep", new=_instant_sleep):
            events = []
            try:
                async for ev in self.client.subscribe_unit_updates():
                    events.append(ev)
                    if len(events) >= 3:
                        raise asyncio.CancelledError()
            except asyncio.CancelledError:
                pass

        self.assertIsInstance(events[0], UnitUpdate)
        self.assertEqual(events[0].message.unit_id, "unit-A")
        self.assertIsInstance(events[1], Reconnected)
        self.assertIsInstance(events[2], UnitUpdate)
        self.assertEqual(events[2].message.unit_id, "unit-B")

    async def test_responds_to_app_level_ping_with_pong(self):
        fake = _FakeWs(
            incoming=[
                _make_text_msg({"type": "ping"}),
                _make_text_msg(_make_unit_update_payload("unit-A")),
            ],
            terminate_with=asyncio.CancelledError(),
        )
        with self._patch_ws_connect([fake]):
            events = []
            try:
                async for ev in self.client.subscribe_unit_updates():
                    events.append(ev)
            except asyncio.CancelledError:
                pass

        # Ping was answered with pong (in addition to the auth message).
        pongs = [m for m in fake.sent if m.get("type") == "pong"]
        self.assertEqual(len(pongs), 1)
        # Ping did not yield a WsEvent — only the UPDATE_UNIT did.
        self.assertEqual(len(events), 1)
        self.assertIsInstance(events[0], UnitUpdate)

    async def test_cancellation_closes_session(self):
        from contextlib import aclosing

        fake = _FakeWs(
            incoming=[_make_text_msg(_make_unit_update_payload("unit-A"))],
            terminate_with=asyncio.CancelledError(),
        )
        holder = []
        with self._patch_ws_connect([fake], fake_session_holder=holder):
            async with aclosing(self.client.subscribe_unit_updates()) as agen:
                try:
                    async for _ in agen:
                        raise asyncio.CancelledError()
                except asyncio.CancelledError:
                    pass
            # aclose() ran the generator's finally, which closed the session.

        self.assertTrue(holder[0].closed)
