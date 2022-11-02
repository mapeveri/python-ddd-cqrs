import abc
from typing import Protocol

from src.marketplace.event.domain.event import Event


class EventResponseRepository(Protocol):
    @abc.abstractmethod
    def save(self, event: Event) -> None:
        ...

    @abc.abstractmethod
    def search(self, start_date: str, end_date: str) -> list:
        ...
