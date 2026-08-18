from apps.events.models import Registration


def registrations_for_email(email):
    return Registration.objects.filter(email__iexact=email).select_related("event")
