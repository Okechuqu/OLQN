from .models import BulletinPage


def latest_bulletin():
    return BulletinPage.objects.live().public().order_by("-bulletin_date").first()
