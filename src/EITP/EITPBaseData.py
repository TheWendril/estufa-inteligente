from enum import Enum
from time import struct_time


class EITPOperation(Enum):
    CONNECT: int = 1
    DISCONNECT: int = 2
    GET: int = 3
    SEND: int = 4
    ENABLE: int = 5
    DISABLE: int = 6
    SYNC: int = 7


class EITPType(Enum):
    SENSOR: int = 1
    ACTUATOR: int = 2
    CLIENT: int = 3
    SERVER: int = 4


class EITPHeader:
    sender: str = None
    recipient: str = None
    operation: EITPOperation = None
    type: EITPType = None


class EITPBody:
    data: float = None
    current_time: str = None


class EITPBaseData:
    header = EITPHeader
    body = EITPBody


class EITPConnectedClient:
    id: int = None
    ip_address: str = None
    last_data: float = None
    refresh: bool = True
    type: EITPType
