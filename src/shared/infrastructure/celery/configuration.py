from flask import Flask
from celery import Celery
from celery.schedules import crontab

from src.marketplace.event.infrastructure.celery.tasks import celery_tasks_events


def configure_celery(app: Flask) -> Celery:
    celery = Celery(
        app.import_name,
        backend=app.config["RESULT_BACKEND"],
        broker=app.config["CELERY_BROKER_URL"],
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    @celery.on_after_configure.connect
    def setup_periodic_tasks(sender, **kwargs):
        pass

    celery_tasks_events(celery)

    celery.conf.beat_schedule = {
        'get-events-every-day-2-am': {
            'task': 'events.provider.get_events',
            'schedule': crontab(minute=0, hour=2),
        },
    }
    celery.conf.timezone = 'UTC'

    return celery
