from .models import Subscriber


def subscribe(email: str):
    return Subscriber.objects.update_or_create(email=email.lower(), defaults={"is_active": True})
