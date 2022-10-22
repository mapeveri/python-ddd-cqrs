from typing import Type

from src.shared.domain.bus.command.command import Command
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.command.command_handler import CommandHandler
from src.shared.infrastructure.persistence.sqlalchemy.utils.transactions import transactional


class MemoryCommandBus(CommandBus):
    def __init__(self):
        self.handlers = {}

    def register(self, command: Type[Command], handler: Type[CommandHandler]):
        self.handlers[command.name()] = handler

    @transactional
    def dispatch(self, command: Command):
        self.handlers[command.name()](command)
