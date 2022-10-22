from typing import Type

from dependency_injector.wiring import Provide
from flask_sqlalchemy import SQLAlchemy

from src.shared.domain.bus.command.command import Command
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.command.command_handler import CommandHandler


class MemoryCommandBus(CommandBus):
    db: SQLAlchemy = Provide['db']

    def __init__(self):
        self.handlers = {}

    def register(self, command: Type[Command], handler: Type[CommandHandler]):
        self.handlers[command.name()] = handler

    def dispatch(self, command: Command):
        try:
            self.db.session.begin_nested()
            self.handlers[command.name()](command)
            self.db.session.commit()
        except Exception as e:
            print("Exception: MemoryCommandBus")
            self.db.session.rollback()
            raise Exception(e)
