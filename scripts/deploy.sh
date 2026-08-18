#!/usr/bin/env sh
set -eu
poetry install --only main
npm ci
npm run build
poetry run python manage.py collectstatic --noinput
poetry run python manage.py migrate
poetry run python manage.py bootstrap_site
