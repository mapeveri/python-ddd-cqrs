from typing import Type, List

from src.shared.domain.bus.event.domain_event import DomainEvent
from src.shared.domain.bus.event.event_bus import EventBus
from src.shared.domain.bus.event.event_handler import EventHandler


class MemoryEventBus(EventBus):
    def __init__(self):
        self.handlers = {}

    def register(self, event: Type[DomainEvent], handler: Type[EventHandler]):
        self.handlers[event.name()] = handler

    def publish(self, events: List[DomainEvent]):
        for event in events:
            self.handlers[event.name()](event)
