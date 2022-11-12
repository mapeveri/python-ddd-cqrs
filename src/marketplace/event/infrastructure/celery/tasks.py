from celery import shared_task
from src.marketplace.event.infrastructure.services.events_provider.process_events_provider import (
    ProcessEventsProvider,
)


@shared_task(name="events.provider.get_events", ignore_result=True)
def provider_get_events() -> None:
    ProcessEventsProvider().process()
