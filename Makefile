.PHONY: install dev migrate migrations superuser css css-watch test lint check docker-up docker-down

install:
	poetry install
	npm install

dev:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate
	poetry run python manage.py bootstrap_site

migrations:
	poetry run python manage.py makemigrations

superuser:
	poetry run python manage.py createsuperuser

css:
	npm run build

css-watch:
	npm run dev

test:
	DJANGO_SETTINGS_MODULE=config.settings.test poetry run python manage.py test

lint:
	poetry run ruff check .

check: lint test
	DJANGO_SETTINGS_MODULE=config.settings.production poetry run python manage.py check --deploy

docker-up:
	docker compose up --build

docker-down:
	docker compose down
