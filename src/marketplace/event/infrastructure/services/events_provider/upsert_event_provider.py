from dataclasses import dataclass
from typing import Optional

from src.marketplace.event.application.command.create.create_event_command import CreateEventCommand
from src.marketplace.event.application.command.update.update_event_command import UpdateEventCommand
from src.marketplace.event.application.query.find.find_event_by_provider_id_query import FindEventByProviderIdQuery
from src.marketplace.event.domain.value_objects.event_id import EventId
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.query.query_bus import QueryBus


@dataclass
class UpsertEventProvider:
    query_bus: QueryBus
    command_bus: CommandBus

    def __call__(
        self,
        provider_event_id: int,
        sell_mode: str,
        provider_organizer_company_id: int,
        title: str,
        event_start_date: str,
        event_end_date: str,
        sell_from: str,
        sell_to: str,
        sold_out: bool,
        zone_list: list
    ):
        event_db = self.query_bus.ask(FindEventByProviderIdQuery(provider_event_id))
        if event_db:
            self._update(provider_event_id,
                         provider_organizer_company_id,
                         title,
                         event_start_date,
                         event_end_date,
                         sell_from, sell_to,
                         sold_out,
                         zone_list)

            return

        self._create(provider_event_id,
                     sell_mode,
                     provider_organizer_company_id,
                     title,
                     event_start_date,
                     event_end_date,
                     sell_from,
                     sell_to,
                     sold_out,
                     zone_list)

    def _create(self,
                provider_event_id: int,
                sell_mode: str,
                provider_organizer_company_id:
                Optional[int],
                title: str,
                event_start_date: str,
                event_end_date: str,
                sell_from: str,
                sell_to: str,
                sold_out: bool,
                zone_list: list) -> None:

        self.command_bus.dispatch(CreateEventCommand(
            EventId.next(),
            provider_event_id,
            sell_mode,
            provider_organizer_company_id if provider_organizer_company_id else None,
            title,
            event_start_date,
            event_end_date,
            sell_from,
            sell_to,
            sold_out,
            zone_list
        ))

    def _update(self,
                provider_event_id: int,
                provider_organizer_company_id:
                Optional[int],
                title: str,
                event_start_date: str,
                event_end_date: str,
                sell_from: str,
                sell_to: str,
                sold_out: bool,
                zone_list: list) -> None:

        self.command_bus.dispatch(UpdateEventCommand(
            provider_event_id,
            provider_organizer_company_id if provider_organizer_company_id else None,
            title,
            event_start_date,
            event_end_date,
            sell_from,
            sell_to,
            sold_out,
            zone_list
        ))
