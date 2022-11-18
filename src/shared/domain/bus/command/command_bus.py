from abc import ABC, abstractmethod
from typing import Type, Union, Any

from src.shared.domain.bus.command.command import Command
from src.shared.domain.bus.command.command_handler import CommandHandler


class CommandBus(ABC):
    @abstractmethod
    def register(self, command: Type[Command], handler: Type[Union[CommandHandler, Any]]) -> None:
        pass

    @abstractmethod
    def dispatch(self, command: Command) -> None:
        pass
