from typing import Dict

from celery import shared_task

from src.shared.infrastructure.bus.event_bus_register import register_domain_events


@shared_task(name="domain_events.handle_event", ignore_result=True)
def event_consumer(event: Dict) -> None:
    print(f"Consuming event: {str(event)}")
    event_name = event["event_name"]
    payload = event["payload"]

    events_mapping = register_domain_events()
    mapping = next(filter(lambda event: event["event"].name() == event_name, events_mapping))
    for event_handler in mapping["handlers"]:
        domain_event = mapping["event"].from_primitives(payload)
        event_handler(domain_event)
