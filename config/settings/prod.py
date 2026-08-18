import sentry_sdk

from .base import *  # noqa: F403

DEBUG = False
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)  # noqa: F405
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31_536_000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

if sentry_dsn := env("SENTRY_DSN", default=""):  # noqa: F405
    sentry_sdk.init(dsn=sentry_dsn, traces_sample_rate=0.1, send_default_pii=False)
