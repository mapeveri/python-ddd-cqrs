from dataclasses import dataclass

from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.event_reponse_repository import EventResponseRepository
from src.marketplace.event.domain.domain_events.event_created_domain_event import EventCreatedDomainEvent
from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.value_objects.mode import Mode
from src.marketplace.event.domain.zone import Zone
from src.shared.domain.bus.event.event_handler import EventHandler


@dataclass
class EventProjectionOnEventCreatedDomainEventHandler(EventHandler):
    event_response_repository: EventResponseRepository

    def __call__(self, event: EventCreatedDomainEvent) -> None:
        zones = list(map(self._create_zone, event.zones, event.aggregate_id))

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
            zones
        )

        self.event_response_repository.save(event)

    def _create_zone(self, zone: dict, event_id: str):
        return Zone.create_from_primitives(
            zone['id'],
            zone['provider_zone_id'],
            zone['capacity'],
            zone['price'],
            zone['name'],
            zone['numbered'],
            event_id
        )
