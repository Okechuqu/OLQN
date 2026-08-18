from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class ProjectIndexPage(Page):
    intro = models.TextField(blank=True)
    subpage_types = ["projects.ProjectPage"]
    content_panels = Page.content_panels + [FieldPanel("intro")]


class ProjectPage(Page):
    summary = models.TextField()
    body = RichTextField(blank=True)
    target_amount = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("summary"), FieldPanel("body"), FieldPanel("target_amount")
    ]
