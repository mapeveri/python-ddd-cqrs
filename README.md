python-ddd-cqrs
===============

Use
---

To start environment using makefile:

    make run

And visit:

    http://localhost:5000/

Migrations
----------

Run migrations manually:

    make run-migrations

Celery task
-----------

To run celery worker and beat:

    docker exec -it marketplace-container pipenv run celery -A app.celery_worker.celery beat --loglevel=DEBUG

    docker exec -it marketplace-container pipenv run celery -A app.celery_worker.celery worker -Q celery --loglevel=DEBUG

Domain events
-------------

To publish outbox events to rabbitmq:

    make run-publish-events

To consume events from rabbitmq:

    make run-consume-events

Events provider
---------------

To get events from provider:

    make run-events-provider

Tests
-----

To run the tests, use make run-tests but first make sure the container is started:

    make run-tests


Monitoring
----------

Access to Grafana and Prometheus:

    grafana: http://localhost:3000/
        user: admin
        password: pass@123

    prometheus: http://localhost:9999/
