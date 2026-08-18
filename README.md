# OLQN Pro-Cathedral

Mobile-first parish website and content platform for Our Lady Queen of Nigeria
Catholic Pro-Cathedral, Garki, Abuja.

## Local setup

```bash
cp .env.example .env
poetry install
poetry run python manage.py migrate
poetry run python manage.py bootstrap_site
poetry run python manage.py createsuperuser
npm install
npm run dev
poetry run python manage.py runserver
```

The development settings use SQLite when `DATABASE_URL` is omitted. Production
requires PostgreSQL and the environment variables documented in `.env.example`.

## Useful commands

```bash
make install       # install Python and frontend dependencies
make migrate       # create/update the database
make dev           # run Django locally
make css           # build minified production CSS
make check         # Django checks, tests and Ruff
```

## Architecture

Each business capability owns its models, services, templates and tests. This
keeps payment, editorial and operational concerns independently testable and
prevents large catch-all Django apps.

- `core`, `home`, `parish`: global CMS infrastructure and parish identity pages
- `clergy`, `worship`, `sacraments`, `ministries`: pastoral content domains
- `bulletins`, `announcements`, `gallery`, `livestream`: publishing domains
- `events`, `tickets`, `payments`, `donations`, `projects`: transactional domains
- `newsletter`, `notifications`, `forms`: communication and submission domains
- `accounts`, `dashboard`, `reports`, `audit`: staff operations and governance
- `templates/`: shared page chrome and small reusable components only
- `static/src/`: repository-owned Tailwind, JavaScript and icons
- `static/dist/`: generated browser assets

The `bulletins` and `donations` Python packages intentionally retain the
historical Django labels `news` and `giving`. This preserves existing migration
history, Wagtail content types and production data while providing the requested
feature-oriented package names.

Settings are split into `development.py`, `production.py` and `test.py`.
Application templates live inside their owning app.

## Containers

```bash
docker compose up --build
```

PostgreSQL data is stored in the named `postgres_data` volume. Local non-Docker
development continues to use SQLite when `DATABASE_URL` is omitted.

See `docs/DELIVERY.md` for the full implementation stages, performance budget,
security constraints and delivery estimate.
