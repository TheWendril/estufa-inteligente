import zmq
from zmq.sugar import socket
from abc import ABC, abstractclassmethod


class EISocket(ABC):

    def __init__(self) -> None:
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)

    @classmethod
    def send(cls, msg: str) -> int:
        pass

    @classmethod
    def receive(cls, msg: str) -> str:
        pass


class EISocketServer(EISocket):

    def bind(self, protocol: str, host: str, port: int) -> None:
        self.socket.bind(str(protocol + '://' + host + ':' + str(port)))

    def receive(self, msg: str) -> str:
        return self.socket.recv().decode()

    def send(self, msg: str):
        return self.socket.send(bytes(msg))


class EISocketClient(EISocket):

    def connect(self, protocol: str, host: str, port: int) -> None:
        self.socket.connect(str(protocol + '://' + host + ':' + str(port)))

    def receive(self, msg: str) -> str:
        return self.socket.recv().decode()

    def send(self, msg: str) -> int:
        return self.socket.send(bytes(msg))