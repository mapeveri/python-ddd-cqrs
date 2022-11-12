from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass
from typing import List, Dict, Optional

from src.marketplace.event.domain.domain_events.event_created_domain_event import (
    EventCreatedDomainEvent,
)
from src.marketplace.event.domain.domain_events.event_updated_domain_event import (
    EventUpdatedDomainEvent,
)
from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.value_objects.mode import Mode
from src.marketplace.event.domain.value_objects.zone_id import ZoneId
from src.marketplace.event.domain.zone import Zone
from src.shared.domain.aggregate.aggregate_root import AggregateRoot
from src.shared.domain.value_objects.price import Price


@dataclass
class Event(AggregateRoot):
    id: EventId
    provider_id: int
    mode: Mode
    provider_organizer_company_id: int
    title: str
    start_date: datetime
    end_date: datetime
    sell_from: datetime
    sell_to: datetime
    sold_out: bool
    zones: Optional[List[Zone]] = None

    @classmethod
    def create(
        cls,
        event_id: EventId,
        provider_id: int,
        mode: Mode,
        provider_organizer_company_id: int,
        title: str,
        start_date: datetime,
        end_date: datetime,
        sell_from: datetime,
        sell_to: datetime,
        sold_out: bool,
        zones: List[dict[str, int, int, float, str, bool, str]],
    ) -> Event:
        event_zones = list(map(lambda zone: cls.make_zone(zone, event_id), zones))

        event = cls(
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
            event_zones,
        )

        event.record(
            EventCreatedDomainEvent(
                event_id.id,
                provider_id,
                mode.value(),
                provider_organizer_company_id,
                title,
                start_date,
                end_date,
                sell_from,
                sell_to,
                sold_out,
                zones,
            )
        )

        return event

    def update(
        self,
        provider_organizer_company_id: int,
        title: str,
        start_date: datetime,
        end_date: datetime,
        sell_from: datetime,
        sell_to: datetime,
        sold_out: bool,
        zones: List[Zone],
    ) -> None:
        self.provider_organizer_company_id = provider_organizer_company_id
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.sell_from = sell_from
        self.sell_to = sell_to
        self.sold_out = sold_out
        self.zones = zones

        zones_primitives = list(map(lambda zone: zone.to_primitives(), zones))

        self.record(
            EventUpdatedDomainEvent(
                self.id.id,
                self.provider_id,
                provider_organizer_company_id,
                self.mode.value(),
                title,
                start_date,
                end_date,
                sell_from,
                sell_to,
                sold_out,
                zones_primitives,
            )
        )

    @classmethod
    def make_zone(cls, zone: Dict, event_id: EventId) -> Zone:
        return Zone.create(
            ZoneId(zone["id"]),
            zone["provider_zone_id"],
            zone["capacity"],
            Price(zone["price"]),
            zone["name"],
            zone["numbered"],
            event_id,
        )

    def calculate_prices(self) -> Dict:
        prices = list(map(lambda zone: zone.price.value(), self.zones))

        return {"min_price": min(prices), "max_price": max(prices)}
