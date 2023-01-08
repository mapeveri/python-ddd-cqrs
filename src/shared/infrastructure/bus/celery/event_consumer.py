from typing import Dict

from celery import shared_task

from src.shared.infrastructure.bus.event.mapping import events_mapping


@shared_task(name="domain_events.handle_event", ignore_result=True)
def event_consumer(event: Dict) -> None:
    print(f"Consuming event: {str(event)}")
    event_name = event["event_name"]
    payload = event["payload"]

    mapping = next(filter(lambda event: event["event"].name() == event_name, events_mapping()))
    for event_handler in mapping["handlers"]:
        event_handler(mapping["event"].from_primitives(payload))
