import asyncio
import unittest
from cool_open_client.cool_automation_client import CoolAutomationClient


class CoolAutomationClientTest(unittest.TestCase):
    def test_client_call(self):
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(CoolAutomationClient.authenticate(username="a", password="aaa"))
        # response = await CoolAutomationClient.authenticate(username="aa", password="aaa")
        print(response)


if __name__ == "__main__":
    unittest.main()
