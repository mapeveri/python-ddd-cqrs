from typing import Type

from dependency_injector.wiring import inject, Provide

from src.marketplace.event.application.command.create.create_event_command import (
    CreateEventCommand,
)
from src.marketplace.event.application.command.projection.create_event_response_command import (
    CreateEventResponseCommand,
)
from src.marketplace.event.application.command.projection.update_event_response_command import (
    UpdateEventResponseCommand,
)
from src.marketplace.event.application.command.update.update_event_command import (
    UpdateEventCommand,
)
from src.marketplace.event.application.command.upload.upload_event_file_command import UploadEventFileCommand
from src.marketplace.retention.application.command.new_event_available.send_email_new_event_available_command import (
    SendEmailNewEventAvailableCommand,
)
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.command.command_handler import CommandHandler
from src.shared.infrastructure.di.container import DI


@inject
def register_commands(
    command_bus: CommandBus = Provide[DI.buses.command_bus],
    create_event_command_handler: Type[CommandHandler] = Provide[DI.handlers.create_event_command_handler],
    update_event_command_handler: Type[CommandHandler] = Provide[DI.handlers.update_event_command_handler],
    create_event_response_command_handler: Type[CommandHandler] = Provide[
        DI.handlers.create_event_response_command_handler
    ],
    update_event_response_command_handler: Type[CommandHandler] = Provide[
        DI.handlers.update_event_response_command_handler
    ],
    upload_file_command_handler: Type[CommandHandler] = Provide[DI.handlers.upload_file_command_handler],
    send_email_new_event_available_command: Type[CommandHandler] = Provide[
        DI.handlers.send_email_new_event_available_command_handler
    ],
) -> None:
    command_bus.register(CreateEventCommand, create_event_command_handler)
    command_bus.register(UpdateEventCommand, update_event_command_handler)
    command_bus.register(CreateEventResponseCommand, create_event_response_command_handler)
    command_bus.register(UpdateEventResponseCommand, update_event_response_command_handler)
    command_bus.register(UploadEventFileCommand, upload_file_command_handler)
    command_bus.register(SendEmailNewEventAvailableCommand, send_email_new_event_available_command)
