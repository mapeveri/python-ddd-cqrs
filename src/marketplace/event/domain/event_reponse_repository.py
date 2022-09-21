import abc

from src.marketplace.event.domain.event import Event


class EventResponseRepository(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def save(self, event: Event) -> None:
        ...

    @abc.abstractmethod
    def search(self, start_date: str, end_date: str) -> list:
        ...
