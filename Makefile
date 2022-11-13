run: ## Run container on port configured
	docker-compose up -d

generate-migration: ## Generate migration
	docker exec -it marketplace-container pipenv run flask db migrate

run-migrations: ## Run migrations
	docker exec -it marketplace-container pipenv run flask db upgrade

run-publish-events: ## Run publish domain events
	docker exec -it marketplace-container pipenv run flask shared publish-events-console-command --limit=200

run-events-provider: ## Run celery to get provider events
	docker exec -it marketplace-container pipenv run celery -A app.celery_worker.celery call events.provider.get_events && docker exec -it marketplace-container pipenv run celery -A app.celery_worker.celery worker --loglevel=DEBUG

run-tests: ## Run tests
	docker exec -it marketplace-container pipenv run python -m unittest discover ./tests -p '*_test.py'

run-style-analysis: ## Run style/analysis
	docker exec -it marketplace-container pipenv run tox -e black && docker exec -it marketplace-container pipenv run tox -e flake8 && docker exec -it marketplace-container pipenv run tox -e mypy
