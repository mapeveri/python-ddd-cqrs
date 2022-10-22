import json
from pydoc import locate

import click
from dependency_injector.wiring import inject, Provide

from src.shared.domain.bus.event.event_bus import EventBus
from src.shared.domain.outbox.outbox_repository import OutboxRepository
from src.shared.infrastructure.di.container import DI


@click.command()
@inject
def publish_events_console_command(
        outbox_repository: OutboxRepository = Provide[DI.outbox_repository],
        event_bus: EventBus = Provide[DI.event_bus]
) -> None:
    outbox_events = outbox_repository.find_all_by_order_by_created_at_asc()
    for outbox_event in outbox_events:
        domain_event = outbox_event.type
        payload = json.loads(outbox_event.payload)

        klass = locate(domain_event)
        event = klass.from_primitives(payload)
        event_bus.execute_handler(event)

        outbox_repository.remove(outbox_event.id)
