from abc import ABC


class Query(ABC):
    @classmethod
    def name(cls):
        return cls.__name__
