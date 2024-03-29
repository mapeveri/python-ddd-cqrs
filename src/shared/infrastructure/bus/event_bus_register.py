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
def register_domain_events(
    event_projection_on_event_created_domain_event_handler: Type[EventHandler] = Provide(
        DI.handlers.event_projection_on_event_created_domain_event_handler
    ),
    event_projection_on_event_updated_domain_event_handler: Type[EventHandler] = Provide(
        DI.handlers.event_projection_on_event_updated_domain_event_handler
    ),
    send_email_new_event_available_on_event_created_domain_event_handler: Type[EventHandler] = Provide(
        DI.handlers.send_email_new_event_available_on_event_created_domain_event_handler
    ),
) -> List[Dict]:
    return [
        {
            "event": EventCreatedDomainEvent,
            "handlers": [
                event_projection_on_event_created_domain_event_handler,
                send_email_new_event_available_on_event_created_domain_event_handler,
            ],
        },
        {
            "event": EventUpdatedDomainEvent,
            "handlers": [event_projection_on_event_updated_domain_event_handler],
        },
    ]
