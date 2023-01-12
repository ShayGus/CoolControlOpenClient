import unittest
from time import sleep
import asyncio
from cool_open_client.cool_automation_client import CoolAutomationClient



class TestWebSocket(unittest.TestCase):
    def setUp(self):
        with open("token.txt") as token_file:
            self.token = token_file.read()
        self.loop = asyncio.get_event_loop()

    def test_websocket(self):
        client = self.loop.run_until_complete(CoolAutomationClient.create(self.token))
        client.open_socket()
        # sleep(60)
        # self.loop.run_until_complete(task)


if __name__ == "__main__":
    unittest.main()
