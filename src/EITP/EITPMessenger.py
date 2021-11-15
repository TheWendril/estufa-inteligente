import EITPbaseData
import EITPTranslator
from ABC import abc
from src.sockets import EiSocket

DEFAULT_PORT = 35000
# MOH PREGUIÇA DE CONTINUAR NAMORAL KKKKKKK

class EITPMessenger(abc):
    pass


class EITPMessengerServer(EITPMessenger):

    def __init__(self):
        self.socket_server = EiSocket.EISocketServer()
        self.socket_server.bind(protocol='tcp', host='127.0.0.1', port=DEFAULT_PORT)

    def start(self, condition_variable: bool) -> None:
        while condition_variable:
            self.socket_server.receive(EiSocket.DEFAULT_LENGTH)


class EITPMessengerClient(EITPMessenger):

    def __init__(self, host: str, port: int):
        self.socket_client = EiSocket.EISocketClient()
        self.socket_client.connect(protocol='tcp', host=host, port=port)

    def connect(self):
        self.socket_client.connect(protocol='tcp', host=host, port=port)



