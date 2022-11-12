from __future__ import annotations

from abc import ABC
from typing import List, Optional, Any

from src.shared.domain.bus.event.domain_event import DomainEvent


class AggregateRoot(ABC):
    def __init__(self) -> None:
        self.domain_events: List = []

    def __new__(cls, *args: Optional[Any], **kwargs: Optional[Any]) -> AggregateRoot:
        cls.domain_events = []
        return super().__new__(cls)

    def pull_domain_events(self) -> List:
        domain_events = self.domain_events
        self.domain_events = []

        return domain_events

    def record(self, domain_event: DomainEvent) -> None:
        self.domain_events.append(domain_event)
