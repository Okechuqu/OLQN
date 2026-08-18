"""Run with `poetry run python scripts/seed_demo.py` after Django setup."""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django  # noqa: E402

django.setup()

from django.core.management import call_command  # noqa: E402

call_command("bootstrap_site")
