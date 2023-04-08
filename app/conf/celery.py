from typing import Any

from flask import Flask
from celery import Celery
from celery.messaging import establish_connection
from celery.schedules import crontab
from kombu import Exchange, Queue


def __configure_cronjobs() -> dict:
    return {
        "get-events-every-day-2-am": {
            "task": "events.provider.get_events",
            "schedule": crontab(minute=0, hour=2),
        },
    }


def configure_celery(app: Flask) -> Celery:
    celery = Celery(app.import_name)
    celery.conf.update(app.config)
    celery.autodiscover_tasks(
        [
            "src.marketplace.event.infrastructure.celery.tasks",
            "src.shared.infrastructure.bus.celery.event_consumer",
        ]
    )

    class ContextTask(celery.Task):
        def __call__(self, *args: Any, **kwargs: Any) -> Any:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    celery.conf.beat_schedule = __configure_cronjobs()
    celery.conf.timezone = "UTC"

    event_exchange = Exchange("events", type="topic")

    event_routing_key = "marketplace.events"
    event_queue = Queue(event_routing_key, exchange=event_exchange, routing_key="#")

    conn = establish_connection(connect_timeout=10)
    event_queue.maybe_bind(conn)
    event_queue.declare()

    celery.conf.task_queues = (event_queue,)
    celery.conf.event_exchange = event_exchange
    celery.conf.event_routing_key = event_routing_key

    return celery
