from django.apps import AppConfig


class DonationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.donations"
    label = "giving"  # Preserve existing donation table and migration history.
    verbose_name = "Donations"
