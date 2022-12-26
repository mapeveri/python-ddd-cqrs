from typing import List

import json

from prometheus_client import Counter

from src.shared.domain.bus.event.domain_event import DomainEvent
from src.shared.domain.bus.event.event_bus import EventBus
from src.shared.domain.outbox.outbox import Outbox
from src.shared.domain.outbox.outbox_repository import OutboxRepository
from src.shared.domain.value_objects.outbox_id import OutboxId

domain_event_metric = Counter('domain_events', 'Domain Events', ['name'])


class MemoryEventBus(EventBus):
    def __init__(self, outbox_repository: OutboxRepository) -> None:
        self.outbox_repository = outbox_repository

    def publish(self, events: List[DomainEvent]) -> None:
        for event in events:
            outbox = Outbox.create(
                OutboxId(OutboxId.next()),
                event.aggregate_type(),
                event.aggregate_id,
                f"{event.__module__}.{event.name()}",
                json.dumps(vars(event), default=str),
            )

            self.outbox_repository.save(outbox)
            domain_event_metric.labels(name=event.event_name()).inc()
