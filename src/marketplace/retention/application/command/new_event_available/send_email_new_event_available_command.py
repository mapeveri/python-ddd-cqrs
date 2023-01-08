from dataclasses import dataclass

from src.shared.domain.bus.command.command import Command


@dataclass(frozen=True)
class SendEmailNewEventAvailableCommand(Command):
    title: str
