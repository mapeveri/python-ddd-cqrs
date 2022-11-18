from typing import Type, Dict, Union, Any

from src.shared.domain.bus.command.command import Command
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.command.command_handler import CommandHandler


class MemoryCommandBus(CommandBus):
    def __init__(self) -> None:
        self.handlers: Dict = {}

    def register(self, command: Type[Command], handler: Type[Union[CommandHandler, Any]]) -> None:
        self.handlers[command.name()] = handler

    def dispatch(self, command: Command) -> None:
        self.handlers[command.name()](command)
