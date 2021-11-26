from src.EITP.EITPBaseData import EITPOperation, EITPBaseData
from src.EITP.EITPMessengerBase import EITPMessengerServer
from abc import ABC
import random


# define a base command class
class Command(ABC):

    @classmethod
    def execute(cls, server: EITPMessengerServer) -> None:
        pass


# a invoker to be used in EITPMessengerServer
class CommandInvoker:

    def __init__(self):
        self.command: Command = None

    def set_command(self, operation: EITPOperation):
        if operation == EITPOperation.GET:
            self.command = GetCommand()

    def execute_command(self) -> None:
        self.command.execute()


# on next, each command class implementation represents a requisition type
# on EITP protocol


class GetCommand(Command):

    def execute(self, server: EITPMessengerServer) -> None:
        pass


class SendCommand(Command):

    def execute(self, server: EITPMessengerServer) -> None:
        pass


class SyncCommand(Command):

    def execute(self, server: EITPMessengerServer) -> None:
        pass


class EnableCommand(Command):

    def execute(self, server: EITPMessengerServer) -> None:
        pass


class DisableCommand(Command):

    def execute(self, server: EITPMessengerServer) -> None:
        pass


class ConnectCommand(Command):

    def execute(self, server: EITPMessengerServer) -> int:
        return random.random()


class DisconnectCommand(Command):

    def execute(self, server: EITPMessengerServer) -> int:
        pass
