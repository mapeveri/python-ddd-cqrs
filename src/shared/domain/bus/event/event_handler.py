from abc import ABC, abstractmethod

from src.shared.domain.bus.event.domain_event import DomainEvent


class EventHandler(ABC):
    @abstractmethod
    def __call__(self, event: DomainEvent) -> None:
        pass
