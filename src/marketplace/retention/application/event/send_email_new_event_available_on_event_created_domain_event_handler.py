from src.marketplace.event.domain.domain_events.event_created_domain_event import (
    EventCreatedDomainEvent,
)
from src.marketplace.retention.application.command.new_event_available.send_email_new_event_available_command import (
    SendEmailNewEventAvailableCommand,
)
from src.marketplace.retention.domain.email_idempotence_repository import EmailIdempotenceRepository
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.event.event_handler import EventHandler


class SendEmailNewEventAvailableOnEventCreatedDomainEventHandler(EventHandler):
    def __init__(self, command_bus: CommandBus, email_idempotence_repository: EmailIdempotenceRepository) -> None:
        self.__command_bus = command_bus
        self.__email_idempotence_repository = email_idempotence_repository

    def __call__(self, event: EventCreatedDomainEvent) -> None:
        key = self.__class__.__name__
        event_id = event.event_id
        emails_sent = self.__email_idempotence_repository.get(key)

        if emails_sent is None:
            emails_sent = []

        if event_id in emails_sent:
            return

        self.__email_idempotence_repository.set(key, event_id)
        self.__command_bus.dispatch(SendEmailNewEventAvailableCommand(event.title))
