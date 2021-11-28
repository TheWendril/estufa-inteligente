from src.EITP.EITPBaseData import EITPOperation, EITPBaseData, EITPConnectedClient, EITPType
from src.EITP.EITPMessengerBase import EITPMessengerServer
from abc import ABC
import random


# define a base command class
class Command(ABC):

    @classmethod
    def execute(cls, server: EITPMessengerServer, message: EITPBaseData) -> None:
        pass


# a invoker to be used in EITPMessengerServer
class CommandInvoker:

    def __init__(self):
        self.command: Command = None

    def set_command(self, operation: EITPOperation):
        if operation == EITPOperation.GET:
            self.command = GetCommand()
        if operation == EITPOperation.SEND:
            self.command = SendCommand()
        if operation == EITPOperation.ENABLE:
            self.command = EnableCommand()
        if operation == EITPOperation.DISABLE:
            self.command = DisableCommand()
        if operation == EITPOperation.SYNC:
            self.command = SyncCommand()
        if operation == EITPOperation.CONNECT:
            self.command = ConnectCommand()
        if operation == EITPOperation.DISCONNECT:
            self.command = DisableCommand()

    def execute_command(self, server: EITPMessengerServer, message: EITPBaseData) -> None:
        self.command.execute(server, message)


# on next, each command class implementation represents a requisition type
# on EITP protocol


class GetCommand(Command):

    def execute(self, server: EITPMessengerServer, message: EITPBaseData) -> None:
        for client in server.connected_clients:
            if client.id == message.header.recipient:
                server.socket_server.send(str(client.last_data))


class SendCommand(Command):

    def execute(self, server: EITPMessengerServer, message: EITPBaseData) -> None:
        for client in server.connected_clients:
            if client.id == message.header.sender:
                client.last_data = message.body.data
                print('Server receive data from ' + client.rotule)


class SyncCommand(Command):

    def execute(self, server: EITPMessengerServer, message: EITPBaseData) -> None:
        if client.id == message.header.sender:
            server.socket_server.send(str(client.last_data))


class EnableCommand(Command):

    def execute(self, server: EITPMessengerServer, message: EITPBaseData) -> None:
        for client in server.connected_clients:
            if client.id == message.header.recipient:
                client.last_data = 1.0
                server.socket_server.send('1')


class DisableCommand(Command):

    def execute(self, server: EITPMessengerServer, message: EITPBaseData) -> None:
        if client.id == message.header.recipient:
            client.last_data = 0.0
            server.socket_server.send('1')


class ConnectCommand(Command):

    def execute(self, server: EITPMessengerServer, message: EITPBaseData) -> None:
        new_client = EITPConnectedClient()
        new_client.id = random.randrange(0, 10000, 1)
        new_client.type = message.header.type
        new_client.rotule = message.header.rotule
        server.connected_clients.insert(0, new_client)
        print('A client with rotule: ' + new_client.rotule + ' has been added')
        # !! add a ip address in future
        server.socket_server.send(str(new_client.id))


class DisconnectCommand(Command):

    def execute(self, server: EITPMessengerServer, message: EITPBaseData) -> None:
        for client in server.connected_clients:
            if client.id == message.header.sender:
                index_to_remove = server.connected_clients.index(client)
                server.connected_clients.pop(index_to_remove)
                server.socket_server.send('1')
