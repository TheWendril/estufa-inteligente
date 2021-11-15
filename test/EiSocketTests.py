import sys
import unittest
from src.sockets.EiSocket import EISocketClient, EISocketServer


class EiSocketTest(unittest.TestCase):

    def __init__(self) -> None:
        super().__init__()
        self.server = EISocketServer()
        self.client = EISocketClient()

    def test_send_data_client_to_server(self):
        pass

    def test_send_data_server_to_client(self):
        pass


if __name__ == '__main__':
    unittest.main()
