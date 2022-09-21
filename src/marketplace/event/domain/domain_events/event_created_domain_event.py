from __future__ import annotations

from datetime import datetime
from typing import Optional, List

from src.shared.domain.bus.event.domain_event import DomainEvent


class EventCreatedDomainEvent(DomainEvent):
    provider_id: int
    mode: str
    provider_organizer_company_id: Optional[int]
    title: str
    start_date: datetime
    end_date: datetime
    sell_from: datetime
    sell_to: datetime
    sold_out: bool
    zones: List[dict[str, int, int, float, str, bool, str]]

    def __init__(self,
                 aggregate_id: str,
                 provider_id: int,
                 mode: str,
                 provider_organizer_company_id: Optional[int],
                 title: str,
                 start_date: datetime,
                 end_date: datetime,
                 sell_from: datetime,
                 sell_to: datetime,
                 sold_out: bool,
                 zones: List[dict[str, int, int, float, str, bool, str]]) -> None:

        super().__init__(aggregate_id)

        self.title = title
        self.provider_id = provider_id
        self.mode = mode
        self.provider_organizer_company_id = provider_organizer_company_id
        self.start_date = start_date
        self.end_date = end_date
        self.sell_from = sell_from
        self.sell_to = sell_to
        self.sold_out = sold_out
        self.zones = zones

    def __eq__(self, other):
        return self.aggregate_id == other.aggregate_id and \
            self.provider_id == other.provider_id and \
            self.mode == other.mode and \
            self.provider_organizer_company_id == other.provider_organizer_company_id and \
            self.title == other.title and \
            self.start_date == other.start_date and \
            self.end_date == other.end_date and \
            self.sell_from == other.sell_from and \
            self.sell_to == other.sell_to and \
            self.sold_out == other.sold_out and \
            self.zones == other.zones
