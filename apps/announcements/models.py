from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from apps.bulletins.models import AnnouncementPage


class AnnouncementIndexPage(Page):
    template = "announcements/announcement_index_page.html"
    intro = models.TextField(blank=True)
    subpage_types = ["news.AnnouncementPage"]
    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["announcements"] = (
            AnnouncementPage.objects.live().public().order_by("-published_at")
        )
        return context


__all__ = ["AnnouncementIndexPage", "AnnouncementPage"]
