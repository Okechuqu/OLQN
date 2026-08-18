from apps.events.models import Registration


def dashboard_totals():
    return {"registrations": Registration.objects.count()}
