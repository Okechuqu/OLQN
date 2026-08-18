from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.documents import get_document_model_string
from wagtail.fields import RichTextField
from wagtail.models import Page


class BulletinIndexPage(Page):
    template = "bulletins/bulletin_index_page.html"
    intro = models.TextField(blank=True)
    subpage_types = ["news.BulletinPage"]
    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["bulletins"] = BulletinPage.objects.child_of(self).live().public().order_by(
            "-bulletin_date"
        )
        return context


class BulletinPage(Page):
    template = "bulletins/bulletin_page.html"
    bulletin_date = models.DateField()
    summary = models.CharField(max_length=240, blank=True)
    document = models.ForeignKey(
        get_document_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content_panels = Page.content_panels + [
        FieldPanel("bulletin_date"), FieldPanel("summary"), FieldPanel("document")
    ]


class AnnouncementPage(Page):
    template = "announcements/announcement_page.html"
    published_at = models.DateField()
    body = RichTextField()
    content_panels = Page.content_panels + [FieldPanel("published_at"), FieldPanel("body")]
