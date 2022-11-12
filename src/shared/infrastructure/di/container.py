from celery import Celery
from dependency_injector import containers, providers
from elasticsearch import Elasticsearch
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.marketplace.event.application.command.create.create_event_command_handler import \
    CreateEventCommandHandler
from src.marketplace.event.application.command.update.update_event_command_handler import UpdateEventCommandHandler
from src.marketplace.event.application.event.event_projection_on_event_created_domain_event_handler import \
    EventProjectionOnEventCreatedDomainEventHandler
from src.marketplace.event.application.event.event_projection_on_event_updated_domain_event_handler import \
    EventProjectionOnEventUpdatedDomainEventHandler
from src.marketplace.event.application.query.find.find_event_by_provider_id_query_handler import \
    FindEventByProviderIdQueryHandler
from src.marketplace.event.application.query.search_events.search_events_query_handler import SearchEventsQueryHandler
from src.marketplace.event.infrastructure.persistence.elasticsearch.repository.elasticsearch_event_response_repository import \
    ElasticsearchEventResponseRepository
from src.marketplace.event.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_event_repository import \
    SqlAlchemyEventRepository
from src.marketplace.event.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_zone_repository import \
    SqlAlchemyZoneRepository
from src.shared.infrastructure.bus.memory_command_bus import MemoryCommandBus
from src.shared.infrastructure.bus.memory_event_bus import MemoryEventBus
from src.shared.infrastructure.bus.memory_query_bus import MemoryQueryBus
from src.shared.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_outbox_repository import \
    SqlAlchemyOutboxRepository


class Repositories(containers.DeclarativeContainer):
    config = providers.Configuration()

    outbox_repository = providers.Factory(SqlAlchemyOutboxRepository)
    event_repository = providers.Factory(SqlAlchemyEventRepository)
    event_response_repository = providers.Factory(ElasticsearchEventResponseRepository)
    zone_repository = providers.Factory(SqlAlchemyZoneRepository)


class Buses(containers.DeclarativeContainer):
    config = providers.Configuration()
    repositories = providers.DependenciesContainer()

    query_bus = providers.Singleton(MemoryQueryBus)
    command_bus = providers.Singleton(MemoryCommandBus)
    event_bus = providers.Singleton(MemoryEventBus, outbox_repository=repositories.outbox_repository)


class Handlers(containers.DeclarativeContainer):
    config = providers.Configuration()
    buses = providers.DependenciesContainer()
    repositories = providers.DependenciesContainer()

    create_event_command_handler = providers.Factory(CreateEventCommandHandler,
                                                     repository=repositories.event_repository,
                                                     event_bus=buses.event_bus)
    update_event_command_handler = providers.Factory(UpdateEventCommandHandler,
                                                     event_repository=repositories.event_repository,
                                                     zone_repository=repositories.zone_repository,
                                                     event_bus=buses.event_bus)

    search_events_query_handler = providers.Factory(
        SearchEventsQueryHandler,
        event_response_repository=repositories.event_response_repository
    )
    find_event_by_provider_id_query_handler = providers.Factory(
        FindEventByProviderIdQueryHandler,
        event_repository=repositories.event_repository,
    )

    event_projection_on_event_created_domain_event_handler = providers.Factory(
        EventProjectionOnEventCreatedDomainEventHandler,
        event_response_repository=repositories.event_response_repository
    )
    event_projection_on_event_updated_domain_event_handler = providers.Factory(
        EventProjectionOnEventUpdatedDomainEventHandler,
        event_response_repository=repositories.event_response_repository
    )


class DI(containers.DeclarativeContainer):
    config = providers.Configuration()

    app = providers.Dependency(instance_of=Flask)
    db = providers.Dependency(instance_of=SQLAlchemy)
    es = providers.Dependency(instance_of=Elasticsearch)
    celery = providers.Dependency(instance_of=Celery)

    repositories = providers.Container(Repositories)
    buses = providers.Container(Buses, repositories=repositories)
    handlers = providers.Container(Handlers, buses=buses, repositories=repositories)
