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


class SyncCommand(Command):

    def execute(self, server: EITPMessengerServer, message: EITPBaseData) -> None:
        pass


class EnableCommand(Command):

    def execute(self, server: EITPMessengerServer, message: EITPBaseData) -> None:
        pass


class DisableCommand(Command):

    def execute(self, server: EITPMessengerServer, message: EITPBaseData) -> None:
        pass


class ConnectCommand(Command):

    def execute(self, server: EITPMessengerServer, message: EITPBaseData) -> int:
        new_client = EITPConnectedClient()
        new_client.id = random.randrange(0, 10000, 1)
        new_client.type = message.header.type
        server.connected_clients.insert(0, new_client)
        # !! add a ip address in future

        if new_client.type == EITPType.CLIENT:
            server.socket_server.send(str(server.connected_clients))
        else:
            server.socket_server.send(str(new_client.id))


class DisconnectCommand(Command):

    def execute(self, server: EITPMessengerServer, message: EITPBaseData) -> int:
        for client in server.connected_clients:
            if client.id == message.header.sender:
                index_to_remove = server.connected_clients.index(client)
                server.connected_clients.pop(index_to_remove)
