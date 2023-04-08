from typing import Type

from dependency_injector.wiring import inject, Provide

from src.marketplace.event.application.query.find.find_event_by_provider_id_query import (
    FindEventByProviderIdQuery,
)
from src.marketplace.event.application.query.search_events.search_events_query import (
    SearchEventsQuery,
)
from src.shared.domain.bus.query.query_bus import QueryBus
from src.shared.domain.bus.query.query_handler import QueryHandler
from src.shared.infrastructure.di.container import DI


@inject
def register_queries(
    query_bus: QueryBus = Provide[DI.buses.query_bus],
    search_events_query_handler: Type[QueryHandler] = Provide[DI.handlers.search_events_query_handler],
    find_event_by_provider_id_query_handler: Type[QueryHandler] = Provide[
        DI.handlers.find_event_by_provider_id_query_handler
    ],
) -> None:
    query_bus.register(SearchEventsQuery, search_events_query_handler)
    query_bus.register(FindEventByProviderIdQuery, find_event_by_provider_id_query_handler)
