#!/usr/bin/env sh
set -eu
poetry run python manage.py migrate
poetry run python manage.py bootstrap_site
exec poetry run python manage.py runserver 0.0.0.0:8000
