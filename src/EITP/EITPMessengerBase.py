import src.EITP.EITPBaseData
from src.EITP.EITPTranslator import EITPTranslator
from abc import ABC
from src.sockets.EiSocket import EISocketServer, EISocketClient, DEFAULT_LENGTH
from src.EITP.Commander.EITPCommander import CommandInvoker
import time

DEFAULT_PORT = 35000


# EITP Messenger SuperClass
class EITPMessengerBase(ABC):

    def __init__(self, host: str, port: int):
        self.socket_client = EISocketClient()
        self.socket_client.connect(protocol='tcp', host=host, port=port)

    def connect(self) -> int:
        eitp_data = EITPbaseData.EITPBaseData()
        eitp_data.header.operation = EITPbaseData.EITPOperation.CONNECT

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))

    def disconnect(self, id_client_sender: int) -> int:
        eitp_data = EITPbaseData.EITPBaseData()
        eitp_data.header.sender = id_client_sender
        eitp_data.header.operation = EITPbaseData.EITPOperation.DISCONNECT

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))


# exclusive class to servers EITP
class EITPMessengerServer:

    def __init__(self):
        self.socket_server = EISocketServer()
        self.socket_server.bind(protocol='tcp', host='127.0.0.1', port=DEFAULT_PORT)
        self.invoker: CommandInvoker = CommandInvoker()
        self.connected_clients: EITPConnectedClient() = []

    def start(self, condition_variable: bool) -> None:

        while condition_variable:
            eitp_obj = EITPTranslator.toeitpobj(self.socket_server.receive(DEFAULT_LENGTH))
            self.invoker.set_command(eitp_obj.header.operation)
            self.invoker.command.execute(self, eitp_obj)


# EITP messenger for devices/hosts clients which rather get data
# and manage actuators

class EITPMessengerBaseClient(EITPMessengerBase):

    def __init__(self, host: str, port: int):
        super().__init__(host, port)

    def get(self, id_client_sender: int, id_client_recip: int) -> float:
        eitp_data = EITPbaseData.EITPBaseData()
        eitp_data.header.operation = EITPbaseData.EITPOperation.GET
        eitp_data.header.sender = id_client_sender
        eitp_data.header.recipient = id_client_recip

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return float(self.socket_client.receive(DEFAULT_LENGTH))

    def enable(self, id_client_sender: int, id_client_recip: int) -> int:
        eitp_data = EITPbaseData.EITPBaseData()
        eitp_data.header.operation = EITPbaseData.EITPOperation.ENABLE
        eitp_data.header.sender = id_client_sender
        eitp_data.header.recipient = id_client_recip

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))

    def disable(self, id_client_sender: int, id_client_recip: int) -> int:
        eitp_data = EITPbaseData.EITPBaseData()
        eitp_data.header.operation = EITPbaseData.EITPOperation.DISABLE
        eitp_data.header.sender = id_client_sender
        eitp_data.header.recipient = id_client_recip

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))


# EITPMessenger for Sensors
class EITPMessengerBaseSensor(EITPMessengerBase):

    def __init__(self, host: str, port: int):
        super().__init__(host, port)

    def send(self, data: float, id_client: int) -> int:
        eitp_data = EITPbaseData.EITPBaseData()
        eitp_data.header.operation = EITPbaseData.EITPOperation.SEND
        eitp_data.header.sender = id_client
        eitp_data.body.data = data
        eitp_data.body.current_time = time.strftime("%H:%M:%S", time.localtime())

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))


# EITPMessenger for actuators
class EITPMessengerBaseActuator(EITPMessengerBase):

    def __init__(self, host: str, port: int):
        super().__init__(host, port)

    def sync(self, id_client_sender: int) -> int:
        eitp_data = EITPbaseData.EITPBaseData()
        eitp_data.header.operation = EITPbaseData.EITPOperation.SYNC
        eitp_data.header.sender = id_client_sender

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))


# create a general class for all purpose
class EITPMessenger(EITPMessengerBaseActuator, EITPMessengerBaseSensor,
                    EITPMessengerBaseClient):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)
