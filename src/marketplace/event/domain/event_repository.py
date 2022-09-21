import abc
from typing import Optional

from src.marketplace.event.domain.event import Event


class EventRepository(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def save(self, event: Event) -> None:
        ...

    @abc.abstractmethod
    def find_by_provider_id(self, provider_id: int) -> Optional[Event]:
        ...
