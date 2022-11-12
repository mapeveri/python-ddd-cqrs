from __future__ import annotations
from dataclasses import dataclass

from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.value_objects.zone_id import ZoneId
from src.shared.domain.value_objects.price import Price


@dataclass
class Zone:
    id: ZoneId
    provider_zone_id: int
    capacity: int
    price: Price
    name: str
    numbered: bool
    event_id: EventId

    @classmethod
    def create(
        cls,
        zoneId: ZoneId,
        provider_zone_id: int,
        capacity: int,
        price: Price,
        name: str,
        numbered: bool,
        event_id: EventId,
    ) -> Zone:
        return cls(zoneId, provider_zone_id, capacity, price, name, numbered, event_id)

    def update(self, capacity: int, price: Price, numbered: bool) -> None:
        self.price = price
        self.capacity = capacity
        self.numbered = numbered

    @classmethod
    def create_from_primitives(
        cls,
        zoneId: str,
        provider_zone_id: int,
        capacity: int,
        price: float,
        name: str,
        numbered: bool,
        event_id: str,
    ) -> Zone:
        return cls(
            ZoneId(zoneId),
            provider_zone_id,
            capacity,
            Price(price),
            name,
            numbered,
            EventId(event_id),
        )

    def to_primitives(self) -> dict:
        return {
            "id": str(self.id),
            "provider_zone_id": self.provider_zone_id,
            "capacity": self.capacity,
            "price": self.price.value(),
            "name": self.name,
            "numbered": self.numbered,
            "event_id": str(self.event_id),
        }
