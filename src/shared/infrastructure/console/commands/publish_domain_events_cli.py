import json
from typing import Optional, Dict

from celery import Celery
from dependency_injector.wiring import inject, Provide

from src.shared.domain.outbox.outbox_criteria import OutboxCriteria
from src.shared.domain.outbox.outbox_repository import OutboxRepository
from src.shared.infrastructure.di.container import DI
from src.shared.infrastructure.persistence.sqlalchemy.utils.transactions import (
    transactional,
)


class PublishDomainEventsCli:
    @inject
    def __init__(
        self,
        celery: Celery = Provide[DI.celery],
        outbox_repository: OutboxRepository = Provide[DI.repositories.outbox_repository],
    ) -> None:
        self.__celery = celery
        self.__outbox_repository = outbox_repository
        self.__exchange = celery.conf.event_exchange

    @transactional
    def __call__(self, limit: Optional[int] = None) -> int:
        outbox_criteria = OutboxCriteria(limit)
        outbox_events = self.__outbox_repository.find_by_criteria(outbox_criteria)

        for outbox_event in outbox_events:
            event_name = outbox_event.type.split(".")[-1]
            payload = json.loads(outbox_event.payload)

            self.__publish_event(event_name, payload)

            self.__outbox_repository.remove(outbox_event.id)

        return 1

    def __publish_event(self, event_name: str, payload: Dict):
        event_data = {
            "event_name": event_name,
            "payload": payload,
        }

        self.__celery.send_task(
            "domain_events.handle_event",
            args=(event_data,),
            routing_key=self.__celery.conf.event_routing_key,
            exchange=self.__exchange,
        )
