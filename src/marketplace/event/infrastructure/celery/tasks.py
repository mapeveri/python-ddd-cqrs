from src.marketplace.event.infrastructure.services.events_provider.process_events_provider import ProcessEventsProvider


def celery_tasks_events(celery) -> None:
    @celery.task(name="events.provider.get_events", ignore_result=True)
    def provider_get_events():
        ProcessEventsProvider().process()
