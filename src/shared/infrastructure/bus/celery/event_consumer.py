from typing import Dict

from celery import shared_task

from src.shared.infrastructure.bus.event.mapping import event_mapping


@shared_task(name="domain_events.handle_event", ignore_result=True)
def event_consumer(event: Dict) -> None:
    print(f"Consuming event: {str(event)}")
    event_name = event["event_name"]
    payload = event["payload"]

    events = event_mapping()
    event_handler = next(filter(lambda event: event["event"].name() == event_name, events))
    event_handler["handler"](event_handler["event"].from_primitives(payload))
