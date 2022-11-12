from dataclasses import dataclass

from src.marketplace.event.application.command.create.create_event_command import (
    CreateEventCommand,
)
from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.event_repository import EventRepository
from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.value_objects.mode import Mode
from src.shared.domain.bus.command.command_handler import CommandHandler
from src.shared.domain.bus.event.event_bus import EventBus
from src.shared.domain.utils import ensure_datetime_iso_is_valid


@dataclass
class CreateEventCommandHandler(CommandHandler):
    repository: EventRepository
    event_bus: EventBus

    def __call__(self, command: CreateEventCommand) -> None:
        event_id = EventId(command.id)
        provider_id = command.provider_id
        mode = Mode(command.mode)
        provider_organizer_company_id = command.provider_organizer_company_id
        title = command.title

        start_date = ensure_datetime_iso_is_valid(command.start_date)
        end_date = ensure_datetime_iso_is_valid(command.end_date)
        sell_from = ensure_datetime_iso_is_valid(command.sell_from)
        sell_to = ensure_datetime_iso_is_valid(command.sell_to)

        sold_out = command.sold_out
        zones = command.zones

        event = Event.create(
            event_id,
            provider_id,
            mode,
            provider_organizer_company_id,
            title,
            start_date,
            end_date,
            sell_from,
            sell_to,
            sold_out,
            zones,
        )

        self.repository.save(event)

        self.event_bus.publish(event.pull_domain_events())
