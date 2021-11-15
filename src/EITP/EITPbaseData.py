from enum import Enum
from time import struct_time


class EITPOperation(Enum):
    CONNECT: int = 1
    DISCONNECT: int = 2
    GET: int = 3
    SEND: int = 4
    ENABLE: int = 5
    DISABLE: int = 6


class EITPHeader:
    sender: str
    recipient: str
    operation: EITPOperation


class EITPBody:
    data: float
    current_time: str


class EITPBaseData:
    header = EITPHeader
    body = EITPBody
