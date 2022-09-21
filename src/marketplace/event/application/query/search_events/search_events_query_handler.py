from dataclasses import dataclass
from typing import List

from src.marketplace.event.application.query.search_events.search_events_query import SearchEventsQuery
from src.marketplace.event.application.response.event_response import EventResponse
from src.marketplace.event.application.response.event_response_converter import EventResponseConverter
from src.marketplace.event.domain.event_reponse_repository import EventResponseRepository
from src.shared.domain.bus.query.query_handler import QueryHandler


@dataclass
class SearchEventsQueryHandler(QueryHandler):
    event_response_repository: EventResponseRepository

    def __call__(self, query: SearchEventsQuery) -> List[EventResponse]:
        events = self.event_response_repository.search(query.start_date, query.end_date)
        event_response_convert = EventResponseConverter()
        return event_response_convert(events)
