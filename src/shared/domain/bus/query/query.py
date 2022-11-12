from abc import ABC


class Query(ABC):
    @classmethod
    def name(cls) -> str:
        return cls.__name__
