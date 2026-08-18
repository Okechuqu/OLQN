from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class ProjectIndexPage(Page):
    template = "projects/project_index_page.html"
    intro = models.TextField(blank=True)
    subpage_types = ["projects.ProjectPage"]
    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["projects"] = ProjectPage.objects.child_of(self).live().public()
        return context


class ProjectPage(Page):
    template = "projects/project_page.html"
    summary = models.TextField()
    body = RichTextField(blank=True)
    target_amount = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("summary"), FieldPanel("body"), FieldPanel("target_amount")
    ]
