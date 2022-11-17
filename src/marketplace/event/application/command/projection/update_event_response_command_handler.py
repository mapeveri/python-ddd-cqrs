from datetime import datetime
from dataclasses import dataclass

from src.marketplace.event.application.command.projection.update_event_response_command import (
    UpdateEventResponseCommand,
)
from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.event_reponse_repository import EventResponseRepository
from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.value_objects.mode import Mode
from src.marketplace.event.domain.zone import Zone
from src.shared.domain.bus.command.command_handler import CommandHandler


@dataclass
class UpdateEventResponseCommandHandler(CommandHandler):
    event_response_repository: EventResponseRepository

    def __call__(self, command: UpdateEventResponseCommand) -> None:
        zones = list(map(self.__create_zone, command.zones, command.id))

        event = Event(
            EventId(command.id),
            command.provider_id,
            Mode(command.mode),
            command.provider_organizer_company_id,
            command.title,
            datetime.fromisoformat(command.start_date),
            datetime.fromisoformat(command.end_date),
            datetime.fromisoformat(command.sell_from),
            datetime.fromisoformat(command.sell_to),
            command.sold_out,
            zones,
        )

        self.event_response_repository.save(event)

    def __create_zone(self, zone: dict, event_id: str) -> Zone:
        return Zone.create_from_primitives(
            zone["id"],
            zone["provider_zone_id"],
            zone["capacity"],
            float(zone["price"]),
            zone["name"],
            zone["numbered"],
            event_id,
        )
