from dataclasses import dataclass
from typing import Optional

from src.marketplace.event.application.query.find.find_event_by_provider_id_query import FindEventByProviderIdQuery
from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.event_repository import EventRepository
from src.shared.domain.bus.query.query_handler import QueryHandler


@dataclass
class FindEventByProviderIdQueryHandler(QueryHandler):
    event_repository: EventRepository

    def __call__(self, query: FindEventByProviderIdQuery) -> Optional[Event]:
        return self.event_repository.find_by_provider_id(query.provider_id)
