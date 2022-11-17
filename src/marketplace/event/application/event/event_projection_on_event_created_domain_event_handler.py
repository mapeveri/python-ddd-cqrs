from dataclasses import dataclass

from src.marketplace.event.application.command.projection.create_event_response_command import (
    CreateEventResponseCommand,
)
from src.marketplace.event.domain.domain_events.event_created_domain_event import (
    EventCreatedDomainEvent,
)
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.event.event_handler import EventHandler


@dataclass
class EventProjectionOnEventCreatedDomainEventHandler(EventHandler):
    command_bus: CommandBus

    def __call__(self, event: EventCreatedDomainEvent) -> None:
        command = CreateEventResponseCommand(
            event.aggregate_id,
            event.provider_id,
            event.mode,
            event.provider_organizer_company_id,
            event.title,
            str(event.start_date),
            str(event.end_date),
            str(event.sell_from),
            str(event.sell_to),
            event.sold_out,
            event.zones,
        )

        self.command_bus.dispatch(command)
