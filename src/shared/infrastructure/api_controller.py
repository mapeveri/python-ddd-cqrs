from abc import ABC

from dependency_injector.wiring import inject, Provide

from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.query.query_bus import QueryBus
from src.shared.infrastructure.di.container import DI


class ApiController(ABC):
    query_bus: QueryBus = Provide[DI.query_bus]
    command_bus: CommandBus = Provide[DI.command_bus]

