from src.EITP.EITPBaseData import EITPType, EITPBaseData, EITPOperation, EITPConnectedClient
from src.EITP.EITPTranslator import EITPTranslator
from abc import ABC
from src.sockets.EiSocket import EISocketServer, EISocketClient, DEFAULT_LENGTH
import time

DEFAULT_PORT = 35000


# EITP Messenger SuperClass
class EITPMessengerBase(ABC):

    def __init__(self, host: str, port: int):
        self.socket_client = EISocketClient()
        print('trying connection with the server...')

        try:
            self.socket_client.connect(protocol='tcp', host=host, port=port)
            print('Client Connected!')

        except NameError:
            print('A error has been ocurred on connection')

    def connect(self, client_type: EITPType, rotule: str) -> int:
        eitp_data = EITPBaseData()
        eitp_data.header.operation = EITPOperation.CONNECT
        eitp_data.header.type = client_type
        eitp_data.header.rotule = rotule

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))

    def disconnect(self, id_client_sender: int) -> int:
        eitp_data = EITPBaseData()
        eitp_data.header.sender = id_client_sender
        eitp_data.header.operation = EITPOperation.DISCONNECT

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))


# exclusive class to servers EITP
class EITPMessengerServer:

    def __init__(self):
        self.socket_server = EISocketServer()
        self.socket_server.bind(protocol='tcp', host='127.0.0.1', port=DEFAULT_PORT)

        # its necessary to import the module here because
        # the class definition may is done first
        from src.EITP.Commander.EITPCommander import CommandInvoker
        # end of import

        self.invoker: CommandInvoker = CommandInvoker()
        self.connected_clients: EITPConnectedClient() = []

    def start(self, condition_variable: bool) -> None:

        print('The Server has been started!')
        while condition_variable:
            recv_data = self.socket_server.receive(DEFAULT_LENGTH)
            print('Requisition received...')

            if recv_data == 'get_all_clients':

                clients = []
                for client in self.connected_clients:
                    client_attributes = []
                    client_attributes.insert(0, client.rotule)
                    client_attributes.insert(0, client.id)
                    client_attributes.insert(0, client.last_data)
                    client_attributes.insert(0, client.type.value)
                    clients.insert(0, client_attributes)

                self.socket_server.send(str(clients))

            else:
                eitp_obj = EITPTranslator.toeitpobj(recv_data)
                self.invoker.set_command(eitp_obj.header.operation)
                self.invoker.command.execute(self, eitp_obj)


# EITP messenger for devices/hosts clients which rather get data
# and manage actuators

class EITPMessengerClient(EITPMessengerBase):

    def __init__(self, host: str, port: int):
        super().__init__(host, port)

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


# EITPMessenger for Sensors
class EITPMessengerSensor(EITPMessengerBase):

    def __init__(self, host: str, port: int):
        super().__init__(host, port)

    def send(self, data: float, id_client: int) -> int:
        eitp_data = EITPBaseData()
        eitp_data.header.operation = EITPOperation.SEND
        eitp_data.header.sender = id_client
        eitp_data.body.data = data
        eitp_data.body.current_time = time.strftime("%H:%M:%S", time.localtime())

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        print('Sending ' + str(eitp_data.body.data))
        return int(self.socket_client.receive(DEFAULT_LENGTH))


# EITPMessenger for actuators
class EITPMessengerActuator(EITPMessengerBase):

    def __init__(self, host: str, port: int):
        super().__init__(host, port)

    def sync(self, id_client_sender: int) -> int:
        eitp_data = EITPBaseData()
        eitp_data.header.operation = EITPOperation.SYNC
        eitp_data.header.sender = id_client_sender

        self.socket_client.send(EITPTranslator.tostring(eitp_data))
        return int(float(self.socket_client.receive(DEFAULT_LENGTH)))


# create a general class for all purpose
class EITPMessenger(EITPMessengerActuator, EITPMessengerSensor,
                    EITPMessengerClient):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)
