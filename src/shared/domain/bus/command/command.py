from abc import ABC


class Command(ABC):
    @classmethod
    def name(cls):
        return cls.__name__
