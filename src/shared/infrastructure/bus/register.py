from typing import Type

from dependency_injector.wiring import inject, Provide

from src.marketplace.event.application.command.create.create_event_command import CreateEventCommand
from src.marketplace.event.application.command.update.update_event_command import UpdateEventCommand
from src.marketplace.event.application.query.find.find_event_by_provider_id_query import FindEventByProviderIdQuery
from src.marketplace.event.application.query.search_events.search_events_query import SearchEventsQuery
from src.marketplace.event.domain.domain_events.event_created_domain_event import EventCreatedDomainEvent
from src.marketplace.event.domain.domain_events.event_updated_domain_event import EventUpdatedDomainEvent
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.command.command_handler import CommandHandler
from src.shared.domain.bus.event.event_bus import EventBus
from src.shared.domain.bus.event.event_handler import EventHandler
from src.shared.domain.bus.query.query_bus import QueryBus
from src.shared.domain.bus.query.query_handler import QueryHandler
from src.shared.infrastructure.di.container import DI


@inject
def register_commands(
        command_bus: CommandBus = Provide[DI.command_bus],
        create_event_command_handler: Type[CommandHandler] = Provide[DI.create_event_command_handler],
        update_event_command_handler: Type[CommandHandler] = Provide[DI.update_event_command_handler]
):
    command_bus.register(CreateEventCommand, create_event_command_handler)
    command_bus.register(UpdateEventCommand, update_event_command_handler)


@inject
def register_queries(
        query_bus: QueryBus = Provide[DI.query_bus],
        search_events_query_handler: Type[QueryHandler] = Provide[DI.search_events_query_handler],
        find_event_by_provider_id_query_handler: Type[QueryHandler] = Provide[
            DI.find_event_by_provider_id_query_handler]
):
    query_bus.register(SearchEventsQuery, search_events_query_handler)
    query_bus.register(FindEventByProviderIdQuery, find_event_by_provider_id_query_handler)


@inject
def register_events(
        event_bus: EventBus = Provide[DI.event_bus],
        event_projection_on_event_created_domain_event_handler: Type[EventHandler] = Provide(
            DI.event_projection_on_event_created_domain_event_handler),
        event_projection_on_event_updated_domain_event_handler: Type[EventHandler] = Provide(
            DI.event_projection_on_event_updated_domain_event_handler)
):
    event_bus.register(EventCreatedDomainEvent, event_projection_on_event_created_domain_event_handler)
    event_bus.register(EventUpdatedDomainEvent, event_projection_on_event_updated_domain_event_handler)


def configure_buses() -> None:
    register_commands()
    register_queries()
    register_events()
