run: run-docker-compose run-migrations

run-docker-compose: ## Run container on port configured
	docker-compose up -d

run-migrations: ## Run migrations
	sleep 5 && docker exec -it marketplace-container pipenv run flask --app=apps.api.app db upgrade

run-events-provider: ## Run celery to get provider events
	docker exec -it marketplace-container pipenv run celery -A apps.api.app.celery call events.provider.get_events && docker exec -it marketplace-container pipenv run celery -A apps.api.app.celery worker --loglevel=DEBUG

run-tests: ## Run tests
	docker exec -it marketplace-container pipenv run python -m unittest discover ./tests -p '*_test.py'
