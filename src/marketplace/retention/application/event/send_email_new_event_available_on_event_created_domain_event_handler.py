from src.marketplace.event.domain.domain_events.event_created_domain_event import (
    EventCreatedDomainEvent,
)
from src.marketplace.retention.application.command.new_event_available.send_email_new_event_available_command import (
    SendEmailNewEventAvailableCommand,
)
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.event.event_handler import EventHandler


class SendEmailNewEventAvailableOnEventCreatedDomainEventHandler(EventHandler):
    def __init__(self, command_bus: CommandBus) -> None:
        self.__command_bus = command_bus

    def __call__(self, event: EventCreatedDomainEvent) -> None:
        self.__command_bus.dispatch(SendEmailNewEventAvailableCommand(event.title))
