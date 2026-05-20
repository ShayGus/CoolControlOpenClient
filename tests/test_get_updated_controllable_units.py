from __future__ import annotations

import unittest
from unittest.mock import AsyncMock, MagicMock, patch

try:
    from cool_open_client.cool_automation_client import (
        CoolAutomationClient,
        UnitUpdateMessage,
    )
    from cool_open_client.utils.singleton import SingletonMeta
except ModuleNotFoundError as exc:
    if exc.name == "websocket":
        raise unittest.SkipTest("websocket-client dependency missing")
    raise


def _unit_payload(unit_id: str, **overrides):
    """Build a camelCase API payload for one unit (matches UnitResponseData aliases)."""
    payload = {
        "id": unit_id,
        "name": f"Unit {unit_id}",
        "type": 1,
        "activeFanMode": 1,
        "activeOperationMode": 2,
        "activeOperationStatus": 1,
        "activeSetpoint": 22,
        "activeSwingMode": 0,
        "ambientTemperature": 23,
        "filter": False,
    }
    payload.update(overrides)
    return payload


class GetUpdatedControllableUnitsTest(unittest.IsolatedAsyncioTestCase):
    """Unit tests for the new bulk-update client method. No live API."""

    async def asyncSetUp(self):
        # Bypass CoolAutomationClient.create() so we don't need a real token.
        SingletonMeta._instances.pop(CoolAutomationClient, None)
        self.client = CoolAutomationClient.__new__(CoolAutomationClient)
        self.client.token = "test-token"
        self.client.api_client = MagicMock()
        self.client.api_client.close = AsyncMock()
        # Minimal dictionary stubs (`_transform_message` reads these).
        self.client.fan_modes = MagicMock(get=lambda v: v)
        self.client.operation_modes = MagicMock(get=lambda v: v)
        self.client.operation_statuses = MagicMock(get=lambda v: v)
        self.client.swing_modes = MagicMock(get=lambda v: v)

    async def asyncTearDown(self):
        await self.client.api_client.close()
        SingletonMeta._instances.pop(CoolAutomationClient, None)

    async def test_returns_message_per_unit(self):
        fake_response = MagicMock()
        fake_response.data = {
            "unit-A": _unit_payload("unit-A"),
            "unit-B": _unit_payload("unit-B", activeSetpoint=20, activeSwingMode=1),
        }
        with patch(
            "cool_open_client.cool_automation_client.UnitsApi"
        ) as fake_units_api_cls:
            fake_units_api = fake_units_api_cls.return_value
            fake_units_api.units_get = AsyncMock(return_value=fake_response)

            result = await self.client.get_updated_controllable_units()

        self.assertEqual(set(result.keys()), {"unit-A", "unit-B"})
        for message in result.values():
            self.assertIsInstance(message, UnitUpdateMessage)
        self.assertEqual(result["unit-A"].unit_id, "unit-A")
        # One bulk HTTP call total — the whole point of the new method.
        self.assertEqual(fake_units_api.units_get.await_count, 1)

    async def test_skips_non_controllable_types(self):
        fake_response = MagicMock()
        fake_response.data = {
            "unit-A": _unit_payload("unit-A"),
            "device-X": {"id": "device-X", "type": 2},  # not a unit
        }
        with patch(
            "cool_open_client.cool_automation_client.UnitsApi"
        ) as fake_units_api_cls:
            fake_units_api = fake_units_api_cls.return_value
            fake_units_api.units_get = AsyncMock(return_value=fake_response)

            result = await self.client.get_updated_controllable_units()

        self.assertIn("unit-A", result)
        self.assertNotIn("device-X", result)

    async def test_float_setpoint_normalized_to_int(self):
        """API can return a float setpoint when half-degree mode is enabled.
        normalize_temperature_fields rounds it before strict-int validation."""
        fake_response = MagicMock()
        fake_response.data = {
            "unit-A": _unit_payload("unit-A", activeSetpoint=22.6, ambientTemperature=21.4),
        }
        with patch(
            "cool_open_client.cool_automation_client.UnitsApi"
        ) as fake_units_api_cls:
            fake_units_api = fake_units_api_cls.return_value
            fake_units_api.units_get = AsyncMock(return_value=fake_response)

            result = await self.client.get_updated_controllable_units()

        self.assertIn("unit-A", result)
        # Floats survive normalization → rounded ints in the message.
        # Using 22.6 (not 22.5) to dodge banker's-rounding edge case.
        msg = result["unit-A"]
        self.assertEqual(msg.setpoint, 23)
        self.assertEqual(msg.ambient_temperature, 21)
