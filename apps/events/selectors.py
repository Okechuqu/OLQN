from .models import EventPage


def upcoming_events():
    return EventPage.objects.live().public().order_by("start_at")
