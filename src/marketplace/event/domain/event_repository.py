import abc
from typing import Optional, Protocol

from src.marketplace.event.domain.event import Event


class EventRepository(Protocol):
    @abc.abstractmethod
    def save(self, event: Event) -> None:
        ...

    @abc.abstractmethod
    def find_by_provider_id(self, provider_id: int) -> Optional[Event]:
        ...
