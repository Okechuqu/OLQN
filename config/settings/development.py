from .base import *  # noqa: F403

DEBUG = env.bool("DJANGO_DEBUG", default=True)  # noqa: F405
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
STORAGES["staticfiles"] = {  # noqa: F405
    "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
}
