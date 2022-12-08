from typing import List, Dict, Type

from dependency_injector.wiring import inject, Provide

from src.marketplace.event.domain.domain_events.event_created_domain_event import (
    EventCreatedDomainEvent,
)
from src.marketplace.event.domain.domain_events.event_updated_domain_event import (
    EventUpdatedDomainEvent,
)
from src.shared.domain.bus.event.event_handler import EventHandler
from src.shared.infrastructure.di.container import DI


@inject
def event_mapping(
    event_projection_on_event_created_domain_event_handler: Type[EventHandler] = Provide(
        DI.handlers.event_projection_on_event_created_domain_event_handler
    ),
    event_projection_on_event_updated_domain_event_handler: Type[EventHandler] = Provide(
        DI.handlers.event_projection_on_event_updated_domain_event_handler
    ),
) -> List[Dict]:
    return [
        {
            "event": EventCreatedDomainEvent,
            "handler": event_projection_on_event_created_domain_event_handler,
        },
        {
            "event": EventUpdatedDomainEvent,
            "handler": event_projection_on_event_updated_domain_event_handler,
        },
    ]
