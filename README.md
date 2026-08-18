# OLQN Pro-Cathedral

Mobile-first parish website and content platform for Our Lady Queen of Nigeria
Catholic Pro-Cathedral, Garki, Abuja.

## Local setup

```bash
cp .env.example .env
poetry install
poetry run python manage.py migrate
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

- `config/`: environment settings, root URLs and ASGI/WSGI entry points
- `apps/core/`: shared blocks, site settings, navigation and utilities
- `apps/home/`: Wagtail homepage and reusable landing-page sections
- `apps/parish/`: about, clergy, ministries, sacraments and mass schedules
- `apps/events/`: events, registrations, tickets and Paystack payments
- `apps/news/`: bulletins, announcements and newsletters
- `apps/giving/`: donations, campaigns and payment records
- `templates/`: shared page chrome and app templates
- `static_src/`: Tailwind source, JavaScript and repository-owned assets
- `static/`: generated/collected assets (not hand-edited)
- `media/`: local development uploads only

See `docs/DELIVERY.md` for the full implementation stages, performance budget,
security constraints and delivery estimate.
