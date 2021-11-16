from EITPbaseData import EITPOperation, EITPBaseData
from EITPTranslator import EITPTranslator
from ABC import abc
from src.sockets.EiSocket import EISocketServer, EISocketClient, DEFAULT_LENGTH
import time

DEFAULT_PORT = 35000


class EITPMessenger(abc):
    pass


class EITPMessengerServer(EITPMessenger):

    def __init__(self):
        self.socket_server = EISocketServer()
        self.socket_server.bind(protocol='tcp', host='127.0.0.1', port=DEFAULT_PORT)

    def start(self, condition_variable: bool) -> None:
        while condition_variable:
            eitp_obj = EITPTranslator.toeitpobj(self.socket_server.receive(DEFAULT_LENGTH))
            # Write a response

    def switch(self, case: EITPOperation):
        pass


class EITPMessengerClient(EITPMessenger):

    def __init__(self, host: str, port: int):
        self.socket_client = EISocketClient()
        self.socket_client.connect(protocol='tcp', host=host, port=port)

    def connect(self) -> int:
        eitp_data = EITPBaseData()
        eitp_data.header.operation = EITPOperation.CONNECT

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))

    def disconnect(self) -> int:
        eitp_data = EITPBaseData()
        eitp_data.header.operation = EITPOperation.DISCONNECT

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))

    def send(self, data: float, id_client: int) -> int:
        eitp_data = EITPBaseData()
        eitp_data.header.operation = EITPOperation.SEND
        eitp_data.header.sender = id_client
        eitp_data.body.data = data
        eitp_data.body.current_time = time.strftime("%H:%M:%S", time.localtime())

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))

    def get(self, id_client_sender: int, id_client_recip: int) -> float:
        eitp_data = EITPBaseData()
        eitp_data.header.operation = EITPOperation.GET
        eitp_data.header.sender = id_client_sender
        eitp_data.header.recipient = id_client_recip

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return float(self.socket_client.receive(DEFAULT_LENGTH))

    def enable(self, id_client_sender: int, id_client_recip: int) -> int:
        eitp_data = EITPBaseData()
        eitp_data.header.operation = EITPOperation.ENABLE
        eitp_data.header.sender = id_client_sender
        eitp_data.header.recipient = id_client_recip

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))

    def disable(self, id_client_sender: int, id_client_recip: int) -> int:
        eitp_data = EITPBaseData()
        eitp_data.header.operation = EITPOperation.DISABLE
        eitp_data.header.sender = id_client_sender
        eitp_data.header.recipient = id_client_recip

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))
