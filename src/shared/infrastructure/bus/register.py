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
from src.marketplace.event.application.command.upload.upload_file_command import UploadFileCommand
from src.marketplace.event.application.query.find.find_event_by_provider_id_query import (
    FindEventByProviderIdQuery,
)
from src.marketplace.event.application.query.search_events.search_events_query import (
    SearchEventsQuery,
)
from src.marketplace.event.domain.domain_events.event_created_domain_event import (
    EventCreatedDomainEvent,
)
from src.marketplace.event.domain.domain_events.event_updated_domain_event import (
    EventUpdatedDomainEvent,
)
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.command.command_handler import CommandHandler
from src.shared.domain.bus.event.event_bus import EventBus
from src.shared.domain.bus.event.event_handler import EventHandler
from src.shared.domain.bus.query.query_bus import QueryBus
from src.shared.domain.bus.query.query_handler import QueryHandler
from src.shared.infrastructure.di.container import DI
from src.shared.infrastructure.persistence.sqlalchemy.utils.transactions import transactional


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
) -> None:
    command_bus.register(CreateEventCommand, transactional(create_event_command_handler))
    command_bus.register(UpdateEventCommand, transactional(update_event_command_handler))
    command_bus.register(CreateEventResponseCommand, create_event_response_command_handler)
    command_bus.register(UpdateEventResponseCommand, update_event_response_command_handler)
    command_bus.register(UploadFileCommand, upload_file_command_handler)


@inject
def register_queries(
    query_bus: QueryBus = Provide[DI.buses.query_bus],
    search_events_query_handler: Type[QueryHandler] = Provide[DI.handlers.search_events_query_handler],
    find_event_by_provider_id_query_handler: Type[QueryHandler] = Provide[
        DI.handlers.find_event_by_provider_id_query_handler
    ],
) -> None:
    query_bus.register(SearchEventsQuery, search_events_query_handler)
    query_bus.register(FindEventByProviderIdQuery, find_event_by_provider_id_query_handler)


@inject
def register_events(
    event_bus: EventBus = Provide[DI.buses.event_bus],
    event_projection_on_event_created_domain_event_handler: Type[EventHandler] = Provide(
        DI.handlers.event_projection_on_event_created_domain_event_handler
    ),
    event_projection_on_event_updated_domain_event_handler: Type[EventHandler] = Provide(
        DI.handlers.event_projection_on_event_updated_domain_event_handler
    ),
) -> None:
    event_bus.register(EventCreatedDomainEvent, event_projection_on_event_created_domain_event_handler)
    event_bus.register(EventUpdatedDomainEvent, event_projection_on_event_updated_domain_event_handler)


def configure_buses() -> None:
    register_commands()
    register_queries()
    register_events()
