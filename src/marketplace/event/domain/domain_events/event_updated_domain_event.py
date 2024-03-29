from __future__ import annotations

from datetime import datetime
from typing import Optional, List, Any, Dict

from src.shared.domain.bus.event.domain_event import DomainEvent


class EventUpdatedDomainEvent(DomainEvent):
    provider_id: int
    mode: str
    provider_organizer_company_id: Optional[int]
    title: str
    start_date: datetime
    end_date: datetime
    sell_from: datetime
    sell_to: datetime
    sold_out: bool
    zones: List[Dict[str, int, int, float, str, bool, str]]

    def __init__(
        self,
        aggregate_id: str,
        provider_id: int,
        provider_organizer_company_id: Optional[int],
        mode: str,
        title: str,
        start_date: datetime,
        end_date: datetime,
        sell_from: datetime,
        sell_to: datetime,
        sold_out: bool,
        zones: List[Dict[str, int, int, float, str, bool, str]],
        event_id: Optional[str] = None,
        occurred_on: Optional[str] = None,
    ) -> None:
        super().__init__(aggregate_id, event_id, occurred_on)

        self.title = title
        self.mode = mode
        self.provider_id = provider_id
        self.provider_organizer_company_id = provider_organizer_company_id
        self.start_date = start_date
        self.end_date = end_date
        self.sell_from = sell_from
        self.sell_to = sell_to
        self.sold_out = sold_out
        self.zones = zones

    @staticmethod
    def event_name() -> str:
        return "marketplace.v1.event.domain_event.event_updated_domain_event"

    @staticmethod
    def aggregate_type() -> str:
        return "Event"

    @classmethod
    def from_primitives(cls, payload: Dict[Any, Any]) -> EventUpdatedDomainEvent:
        return cls(
            payload["aggregate_id"],
            payload["provider_id"],
            payload["mode"],
            payload["provider_organizer_company_id"],
            payload["title"],
            datetime.fromisoformat(payload["start_date"]),
            datetime.fromisoformat(payload["end_date"]),
            datetime.fromisoformat(payload["sell_from"]),
            datetime.fromisoformat(payload["sell_to"]),
            payload["sold_out"],
            payload["zones"],
            payload["event_id"],
            payload["occurred_on"],
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EventUpdatedDomainEvent):
            return NotImplemented

        return (
            self.aggregate_id == other.aggregate_id
            and self.provider_id == other.provider_id
            and self.mode == other.mode
            and self.provider_organizer_company_id == other.provider_organizer_company_id
            and self.title == other.title
            and self.start_date == other.start_date
            and self.end_date == other.end_date
            and self.sell_from == other.sell_from
            and self.sell_to == other.sell_to
            and self.sold_out == other.sold_out
            and self.zones == other.zones
        )
