from flask import Flask
from celery import Celery
from celery.schedules import crontab


def configure_cronjobs() -> dict:
    return {
        'get-events-every-day-2-am': {
            'task': 'events.provider.get_events',
            'schedule': crontab(minute=0, hour=2),
        },
    }


def configure_celery(app: Flask) -> Celery:
    celery = Celery(app.import_name)
    celery.conf.update(app.config)
    celery.autodiscover_tasks(['src.marketplace.event.infrastructure.celery.tasks'])

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    celery.conf.beat_schedule = configure_cronjobs()
    celery.conf.timezone = 'UTC'

    return celery
