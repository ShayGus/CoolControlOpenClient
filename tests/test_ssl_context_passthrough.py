"""Verify a caller-supplied SSL context is honored end-to-end.

Home Assistant pre-builds an SSL context off the event loop and passes it
in to avoid blocking I/O during connection setup. These tests assert the
context survives the trip through ApiClient -> RESTClientObject without
the library ever calling `ssl.create_default_context` itself.
"""
from __future__ import annotations

import ssl
import unittest
from unittest.mock import patch

from cool_open_client.client.api_client import ApiClient
from cool_open_client.client.rest import RESTClientObject
from cool_open_client.cool_automation_client import CoolAutomationClient


class SSLContextPassthroughTest(unittest.TestCase):
    def test_api_client_forwards_ssl_context_to_rest_client(self):
        ctx = ssl.create_default_context()
        client = ApiClient(ssl_context=ctx)
        self.assertIs(client.rest_client.ssl_context, ctx)

    def test_rest_client_skips_create_default_context_when_context_supplied(self):
        ctx = ssl.create_default_context()
        with patch("cool_open_client.client.rest.ssl.create_default_context") as m:
            from cool_open_client.client.configuration import Configuration
            RESTClientObject(Configuration.get_default(), ssl_context=ctx)
        # The whole point: we never call the blocking factory when a context is supplied.
        m.assert_not_called()

    def test_rest_client_uses_create_default_context_when_no_context_supplied(self):
        # Backward-compat: without a context, the library still constructs one
        # itself (today's behaviour — callers without HA can keep working).
        with patch(
            "cool_open_client.client.rest.ssl.create_default_context",
            wraps=ssl.create_default_context,
        ) as m:
            from cool_open_client.client.configuration import Configuration
            RESTClientObject(Configuration.get_default())
        m.assert_called_once()

    def test_cool_automation_client_init_forwards_ssl_context(self):
        ctx = ssl.create_default_context()
        client = CoolAutomationClient(ssl_context=ctx)
        self.assertIs(client.api_client.rest_client.ssl_context, ctx)


if __name__ == "__main__":
    unittest.main()
