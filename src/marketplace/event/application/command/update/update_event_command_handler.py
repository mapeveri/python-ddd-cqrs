from dataclasses import dataclass
from typing import Union

from src.marketplace.event.application.command.update.update_event_command import (
    UpdateEventCommand,
)
from src.marketplace.event.domain.event_repository import EventRepository
from src.marketplace.event.domain.services.event_finder_by_provider_id import (
    EventFinderByProviderId,
)
from src.marketplace.event.domain.zone import Zone
from src.marketplace.event.domain.zone_repository import ZoneRepository
from src.shared.domain.bus.command.command_handler import CommandHandler
from src.shared.domain.bus.event.event_bus import EventBus
from src.shared.domain.datetime_utils import ensure_datetime_iso_is_valid
from src.shared.domain.value_objects.price import Price


@dataclass
class UpdateEventCommandHandler(CommandHandler):
    event_repository: EventRepository
    zone_repository: ZoneRepository
    event_bus: EventBus
    finder: EventFinderByProviderId = None

    def __post_init__(self) -> None:
        self.finder = EventFinderByProviderId(self.event_repository)

    def __call__(self, command: UpdateEventCommand) -> None:
        event = self.finder(command.provider_id)

        provider_organizer_company_id = command.provider_organizer_company_id
        title = command.title

        start_date = ensure_datetime_iso_is_valid(command.start_date)
        end_date = ensure_datetime_iso_is_valid(command.end_date)
        sell_from = ensure_datetime_iso_is_valid(command.sell_from)
        sell_to = ensure_datetime_iso_is_valid(command.sell_to)

        sold_out = command.sold_out

        zones = command.zones
        event_zones = self.zone_repository.zones_by_event_id(event.id)
        event_zones_updated = list(map(self.__update_zones, event_zones, zones))

        event.update(
            provider_organizer_company_id,
            title,
            start_date,
            end_date,
            sell_from,
            sell_to,
            sold_out,
            event_zones_updated,
        )

        self.event_repository.save(event)

        self.event_bus.publish(event.pull_domain_events())

    def __update_zones(self, zone: Zone, zones: Union[list, dict]) -> Zone:
        try:
            item_zone = next(filter(lambda z: z["provider_zone_id"] == zone.provider_zone_id, zones))
        except TypeError:
            item_zone = zones if zones["provider_zone_id"] == zone.provider_zone_id else None

        if not item_zone:
            return zone

        zone.update(item_zone["capacity"], Price(item_zone["price"]), item_zone["numbered"])

        return zone
