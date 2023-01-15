import abc
from typing import Optional, Protocol

from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.value_objects.event_id import EventId


class EventRepository(Protocol):
    @abc.abstractmethod
    def find_by_id(self, event_id: EventId) -> Optional[Event]:
        ...

    @abc.abstractmethod
    def find_by_provider_id(self, provider_id: int) -> Optional[Event]:
        ...

    @abc.abstractmethod
    def save(self, event: Event) -> None:
        ...
