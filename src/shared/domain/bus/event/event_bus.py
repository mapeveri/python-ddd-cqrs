from abc import ABC, abstractmethod
from typing import Type, List

from src.shared.domain.bus.event.domain_event import DomainEvent
from src.shared.domain.bus.event.event_handler import EventHandler


class EventBus(ABC):
    @abstractmethod
    def register(self, event: Type[DomainEvent], handler: Type[EventHandler]):
        pass

    @abstractmethod
    def publish(self, events: List[DomainEvent]):
        pass
