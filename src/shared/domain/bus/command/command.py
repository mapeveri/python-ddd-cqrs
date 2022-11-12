from abc import ABC


class Command(ABC):
    @classmethod
    def name(cls) -> str:
        return cls.__name__
