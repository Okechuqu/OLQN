from apps.events.models import Registration


def paid_registrations():
    return Registration.objects.filter(status=Registration.Status.PAID).select_related("event")
