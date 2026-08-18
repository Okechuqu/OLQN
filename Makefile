.PHONY: install dev migrate migrations superuser css css-watch test lint check

install:
	poetry install
	npm install

dev:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

migrations:
	poetry run python manage.py makemigrations

superuser:
	poetry run python manage.py createsuperuser

css:
	npm run build

css-watch:
	npm run dev

test:
	poetry run python manage.py test

lint:
	poetry run ruff check .

check: lint test
	poetry run python manage.py check --deploy
