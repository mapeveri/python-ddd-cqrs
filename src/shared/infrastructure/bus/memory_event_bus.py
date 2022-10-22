from typing import Type, List

import json

from src.shared.domain.bus.event.domain_event import DomainEvent
from src.shared.domain.bus.event.event_bus import EventBus
from src.shared.domain.bus.event.event_handler import EventHandler
from src.shared.domain.outbox.outbox import Outbox
from src.shared.domain.outbox.outbox_repository import OutboxRepository
from src.shared.domain.value_objects.outbox_id import OutboxId


class MemoryEventBus(EventBus):
    def __init__(self, outbox_repository: OutboxRepository):
        self.handlers = {}
        self.outbox_repository = outbox_repository

    def register(self, event: Type[DomainEvent], handler: Type[EventHandler]):
        self.handlers[event.name()] = handler

    def execute_handler(self, event: Type[DomainEvent]) -> None:
        self.handlers[event.name()](event)

    def publish(self, events: List[DomainEvent]):
        for event in events:
            outbox = Outbox.create(
                OutboxId(OutboxId.next()),
                event.aggregate_type(),
                event.aggregate_id,
                f'{event.__module__}.{event.name()}',
                json.dumps(vars(event), default=str)
            )

            self.outbox_repository.save(outbox)
