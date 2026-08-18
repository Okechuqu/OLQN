from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class StreamChannel(models.Model):
    name = models.CharField(max_length=120)
    url = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class LivestreamPage(Page):
    template = "livestream/livestream_page.html"
    intro = models.TextField(blank=True)
    max_count = 1
    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["stream"] = StreamChannel.objects.filter(is_active=True).first()
        return context
