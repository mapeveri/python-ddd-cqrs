from dataclasses import dataclass

from src.marketplace.event.domain.domain_events.event_created_domain_event import (
    EventCreatedDomainEvent,
)
from src.marketplace.retention.application.command.new_event_available.send_email_new_event_available_command import (
    SendEmailNewEventAvailableCommand,
)
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.event.event_handler import EventHandler


@dataclass
class SendEmailNewEventAvailableOnEventCreatedDomainEventHandler(EventHandler):
    command_bus: CommandBus

    def __call__(self, event: EventCreatedDomainEvent) -> None:
        self.command_bus.dispatch(SendEmailNewEventAvailableCommand(event.title))
