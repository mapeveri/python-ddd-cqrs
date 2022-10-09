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

    docker exec -it marketplace-container pipenv run celery -A apps.api.app.celery beat --loglevel=DEBUG

    docker exec -it marketplace-container pipenv run celery -A apps.api.app.celery worker --loglevel=DEBUG


Events
------

To get events from provider:

    make run-events-provider

Tests
-----

To run the tests, use make run-tests but first make sure the container is started:

    make run-tests
