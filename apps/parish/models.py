from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.models import Page


class StandardPage(Page):
    intro = models.TextField(blank=True)
    body = RichTextField(blank=True)
    hero_image = models.ForeignKey(
        get_image_model_string(), null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    content_panels = Page.content_panels + [
        FieldPanel("intro"), FieldPanel("hero_image"), FieldPanel("body")
    ]


class MinistryIndexPage(StandardPage):
    subpage_types = ["parish.MinistryPage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["ministries"] = MinistryPage.objects.child_of(self).live().public()
        return context


class MinistryPage(StandardPage):
    meeting_time = models.CharField(max_length=140, blank=True)
    contact_email = models.EmailField(blank=True)
    content_panels = StandardPage.content_panels + [
        FieldPanel("meeting_time"), FieldPanel("contact_email")
    ]
