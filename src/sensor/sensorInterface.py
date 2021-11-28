from typing import AbstractSet
from abc import ABC, abstractclassmethod


# interface to sensors on client side
# Each sensor must implements the monitoring function


class SensorInterface(ABC):

    sensorID: int = None

    @classmethod
    def monitoring(cls):
        pass


