from abc import ABC


class actuatorInterface(ABC):

    @classmethod
    def enable(cls):
        pass

    @classmethod
    def disable(cls):
        pass