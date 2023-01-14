from typing import List

from src.marketplace.event.application.query.search_events.search_events_query import (
    SearchEventsQuery,
)
from src.marketplace.event.application.response.event_response import EventResponse
from src.marketplace.event.application.response.event_response_converter import EventResponseConverter
from src.marketplace.event.domain.event_reponse_repository import (
    EventResponseRepository,
)
from src.shared.domain.bus.query.query_handler import QueryHandler


class SearchEventsQueryHandler(QueryHandler):
    def __init__(
        self, event_response_repository: EventResponseRepository, event_response_converter: EventResponseConverter
    ) -> None:
        self.__event_response_repository = event_response_repository
        self.__event_response_converter = event_response_converter

    def __call__(self, query: SearchEventsQuery) -> List[EventResponse]:
        events = self.__event_response_repository.search(query.start_date, query.end_date)
        return self.__event_response_converter.convert(events)
