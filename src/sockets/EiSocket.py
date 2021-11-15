import zmq
from zmq.sugar import socket
from abc import ABC, abstractclassmethod
import errno


DEFAULT_LENGTH = 1024


class EISocket(ABC):

    def __init__(self) -> None:
        self.context = zmq.Context()


    @classmethod
    def send(cls, msg: str) -> int:
        pass

    @classmethod
    def receive(cls, strlen: int) -> str:
        pass


class EISocketServer(EISocket):

    def __init__(self):
        super(EISocketServer, self).__init__()
        self.socket = self.context.socket(zmq.REP)

    def bind(self, protocol: str, host: str, port: int) -> None:
        self.socket.bind(str(protocol + '://' + host + ':' + str(port)))

    def receive(self, strlen: int) -> str:
        return self.socket.recv(strlen).decode('utf-8')

    def send(self, msg: str):
        return self.socket.send(msg.encode('utf-8'))


class EISocketClient(EISocket):

    def __init__(self):
        super(EISocketClient, self).__init__()
        self.socket = self.context.socket(zmq.REQ)

    def connect(self, protocol: str, host: str, port: int) -> None:
        self.socket.connect(str(protocol + '://' + host + ':' + str(port)))

    def receive(self, strlen: int) -> str:
        return self.socket.recv(strlen).decode('utf-8')

    def send(self, msg: str) -> int:

        try:
            self.socket.send(msg.encode('utf-8'))
            return 1

        except NameError:
            print(NameError)
            return 0
