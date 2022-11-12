from dataclasses import dataclass

from src.marketplace.event.domain.domain_events.event_updated_domain_event import (
    EventUpdatedDomainEvent,
)
from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.event_reponse_repository import (
    EventResponseRepository,
)
from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.value_objects.mode import Mode
from src.marketplace.event.domain.zone import Zone
from src.shared.domain.bus.event.event_handler import EventHandler


@dataclass
class EventProjectionOnEventUpdatedDomainEventHandler(EventHandler):
    event_response_repository: EventResponseRepository

    def __call__(self, event: EventUpdatedDomainEvent) -> None:
        zones = list(map(self.__zones, event.zones, event.aggregate_id))

        event = Event(
            EventId(event.aggregate_id),
            event.provider_id,
            Mode(event.mode),
            event.provider_organizer_company_id,
            event.title,
            event.start_date,
            event.end_date,
            event.sell_from,
            event.sell_to,
            event.sold_out,
            zones,
        )

        self.event_response_repository.save(event)

    def __zones(self, zone: dict, event_id: str) -> Zone:
        return Zone.create_from_primitives(
            zone["id"],
            zone["provider_zone_id"],
            zone["capacity"],
            float(zone["price"]),
            zone["name"],
            zone["numbered"],
            event_id,
        )
