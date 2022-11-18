from celery import Celery
from dependency_injector import containers, providers
from elasticsearch import Elasticsearch
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.marketplace.event.application.command.create.create_event_command_handler import (
    CreateEventCommandHandler,
)
from src.marketplace.event.application.command.projection.create_event_response_command_handler import (
    CreateEventResponseCommandHandler,
)
from src.marketplace.event.application.command.projection.update_event_response_command_handler import (
    UpdateEventResponseCommandHandler,
)
from src.marketplace.event.application.command.update.update_event_command_handler import (
    UpdateEventCommandHandler,
)
from src.marketplace.event.application.event.event_projection_on_event_created_domain_event_handler import (
    EventProjectionOnEventCreatedDomainEventHandler,
)
from src.marketplace.event.application.event.event_projection_on_event_updated_domain_event_handler import (
    EventProjectionOnEventUpdatedDomainEventHandler,
)
from src.marketplace.event.application.query.find.find_event_by_provider_id_query_handler import (
    FindEventByProviderIdQueryHandler,
)
from src.marketplace.event.application.query.search_events.search_events_query_handler import (
    SearchEventsQueryHandler,
)
from src.marketplace.event.infrastructure.persistence.elasticsearch.repository import (
    ElasticsearchEventResponseRepository,
)
from src.marketplace.event.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_event_repository import (
    SqlAlchemyEventRepository,
)
from src.marketplace.event.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_zone_repository import (
    SqlAlchemyZoneRepository,
)
from src.shared.domain.unit_of_work import UnitOfWork
from src.shared.infrastructure.bus.memory_command_bus import MemoryCommandBus
from src.shared.infrastructure.bus.memory_event_bus import MemoryEventBus
from src.shared.infrastructure.bus.memory_query_bus import MemoryQueryBus
from src.shared.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_outbox_repository import (
    SqlAlchemyOutboxRepository,
)
from src.shared.infrastructure.persistence.sqlalchemy.unit_of_work import SqlAlchemyUnitOfWork


class Repositories(containers.DeclarativeContainer):
    config = providers.Configuration()

    outbox_repository: SqlAlchemyOutboxRepository = providers.Factory(SqlAlchemyOutboxRepository)
    event_repository: SqlAlchemyEventRepository = providers.Factory(SqlAlchemyEventRepository)
    event_response_repository: ElasticsearchEventResponseRepository = providers.Factory(
        ElasticsearchEventResponseRepository
    )
    zone_repository: SqlAlchemyZoneRepository = providers.Factory(SqlAlchemyZoneRepository)


class Buses(containers.DeclarativeContainer):
    config = providers.Configuration()
    repositories = providers.DependenciesContainer()

    query_bus: MemoryQueryBus = providers.Singleton(MemoryQueryBus)
    command_bus: MemoryCommandBus = providers.Singleton(MemoryCommandBus)
    event_bus: MemoryEventBus = providers.Singleton(MemoryEventBus, outbox_repository=repositories.outbox_repository)


class Handlers(containers.DeclarativeContainer):
    config = providers.Configuration()
    buses = providers.DependenciesContainer()
    repositories = providers.DependenciesContainer()

    create_event_command_handler: CreateEventCommandHandler = providers.Factory(
        CreateEventCommandHandler,
        repository=repositories.event_repository,
        event_bus=buses.event_bus,
    )
    update_event_command_handler: UpdateEventCommandHandler = providers.Factory(
        UpdateEventCommandHandler,
        event_repository=repositories.event_repository,
        zone_repository=repositories.zone_repository,
        event_bus=buses.event_bus,
    )

    search_events_query_handler: SearchEventsQueryHandler = providers.Factory(
        SearchEventsQueryHandler,
        event_response_repository=repositories.event_response_repository,
    )
    find_event_by_provider_id_query_handler: FindEventByProviderIdQueryHandler = providers.Factory(
        FindEventByProviderIdQueryHandler,
        event_repository=repositories.event_repository,
    )

    event_projection_on_event_created_domain_event_handler: EventProjectionOnEventCreatedDomainEventHandler = (
        providers.Factory(
            EventProjectionOnEventCreatedDomainEventHandler,
            command_bus=buses.command_bus,
        )
    )
    event_projection_on_event_updated_domain_event_handler: EventProjectionOnEventUpdatedDomainEventHandler = (
        providers.Factory(
            EventProjectionOnEventUpdatedDomainEventHandler,
            command_bus=buses.command_bus,
        )
    )

    create_event_response_command_handler: CreateEventResponseCommandHandler = providers.Factory(
        CreateEventResponseCommandHandler,
        event_response_repository=repositories.event_response_repository,
    )

    update_event_response_command_handler: UpdateEventResponseCommandHandler = providers.Factory(
        UpdateEventResponseCommandHandler,
        event_response_repository=repositories.event_response_repository,
    )


class DI(containers.DeclarativeContainer):
    config = providers.Configuration()

    app = providers.Dependency(instance_of=Flask)
    db = providers.Dependency(instance_of=SQLAlchemy)
    es = providers.Dependency(instance_of=Elasticsearch)
    celery = providers.Dependency(instance_of=Celery)

    unit_of_work: UnitOfWork = providers.Factory(SqlAlchemyUnitOfWork)

    repositories = providers.Container(Repositories)
    buses = providers.Container(Buses, repositories=repositories)
    handlers = providers.Container(Handlers, buses=buses, repositories=repositories)
