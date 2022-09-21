from abc import ABC

from src.shared.domain.bus.event.domain_event import DomainEvent


class AggregateRoot(ABC):
    def __init__(self):
        self.domain_events = []

    def __new__(cls, *args, **kwargs):
        cls.domain_events = []
        return super().__new__(cls)

    def pull_domain_events(self) -> list:
        domain_events = self.domain_events
        self.domain_events = []

        return domain_events

    def record(self, domain_event: DomainEvent) -> None:
        self.domain_events.append(domain_event)
