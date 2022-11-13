import json
from pydoc import locate
from typing import Optional

import click
from dependency_injector.wiring import inject, Provide

from src.shared.domain.bus.event.event_bus import EventBus
from src.shared.domain.outbox.outbox_criteria import OutboxCriteria
from src.shared.domain.outbox.outbox_repository import OutboxRepository
from src.shared.infrastructure.di.container import DI
from src.shared.infrastructure.persistence.sqlalchemy.utils.transactions import (
    transactional,
)


@click.command("publish-events-console-command")
@click.option("--limit", type=click.INT, required=False)
class PublishDomainEventsCli:
    @inject
    def __init__(
        self,
        outbox_repository: OutboxRepository = Provide[DI.repositories.outbox_repository],
        event_bus: EventBus = Provide[DI.buses.event_bus],
        limit: Optional[int] = None,
    ) -> None:
        self.__outbox_repository = outbox_repository
        self.__event_bus = event_bus
        self.__limit = limit
        self.publish()

    @transactional
    def publish(self) -> int:
        outbox_criteria = OutboxCriteria(self.__limit)
        outbox_events = self.__outbox_repository.find_by_criteria(outbox_criteria)

        for outbox_event in outbox_events:
            domain_event = outbox_event.type
            payload = json.loads(outbox_event.payload)

            klass = locate(domain_event)
            event = klass.from_primitives(payload)
            self.__event_bus.execute_handler(event)

            self.__outbox_repository.remove(outbox_event.id)

        return 1
