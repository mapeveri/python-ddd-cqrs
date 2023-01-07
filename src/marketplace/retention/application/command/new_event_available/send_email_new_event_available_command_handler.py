from dataclasses import dataclass

from src.marketplace.retention.application.command.new_event_available.send_email_new_event_available_command import (
    SendEmailNewEventAvailableCommand,
)
from src.marketplace.retention.domain.send_email import SendEmail
from src.shared.domain.bus.command.command_handler import CommandHandler


@dataclass
class SendEmailNewEventAvailableCommandHandler(CommandHandler):
    send_email: SendEmail

    def __call__(self, command: SendEmailNewEventAvailableCommand) -> None:
        self.send_email.send("New event available", f"There is a new event available: {command.title}")
