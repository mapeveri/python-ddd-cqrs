from typing import List

from dependency_injector.wiring import Provide

from src.marketplace.event.infrastructure.services.events_provider.http_events_provider import HttpEventsProvider
from src.marketplace.event.infrastructure.services.events_provider.upsert_event_provider import UpsertEventProvider
from src.marketplace.event.infrastructure.services.events_provider.json_parse_events_provider import \
    JsonParseEventsProvider
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.query.query_bus import QueryBus
from src.shared.infrastructure.di.container import DI


class ProcessEventsProvider:
    query_bus: QueryBus = Provide[DI.query_bus]
    command_bus: CommandBus = Provide[DI.command_bus]
    http_events_provider = HttpEventsProvider = None
    upsert_event_service: UpsertEventProvider = None
    json_parse_events_provider = JsonParseEventsProvider = None

    def __init__(self):
        self.http_events_provider = HttpEventsProvider()
        self.json_parse_events_provider = JsonParseEventsProvider()
        self.upsert_event_service = UpsertEventProvider(self.query_bus, self.command_bus)

    def process(self) -> None:
        data = self.http_events_provider()
        events = self.json_parse_events_provider(data)
        self.__upsert_events_provider(events)

    def __upsert_events_provider(self, events: List[dict]) -> None:
        for event in events:
            self.upsert_event_service(
                event['provider_event_id'],
                event['sell_mode'],
                event['provider_organizer_company_id'],
                event['title'],
                event['event_start_date'],
                event['event_end_date'],
                event['sell_from'],
                event['sell_to'],
                event['sold_out'],
                event['zones'],
            )
