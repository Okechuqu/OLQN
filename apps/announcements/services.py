from apps.bulletins.models import AnnouncementPage


def recent_announcements(limit=5):
    return AnnouncementPage.objects.live().public().order_by("-published_at")[:limit]
