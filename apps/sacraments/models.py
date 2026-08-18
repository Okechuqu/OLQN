from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class SacramentIndexPage(Page):
    template = "sacraments/sacrament_index_page.html"
    intro = models.TextField(blank=True)
    subpage_types = ["sacraments.SacramentPage"]
    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["sacraments"] = SacramentPage.objects.child_of(self).live().public()
        return context


class SacramentPage(Page):
    template = "sacraments/sacrament_page.html"
    intro = models.TextField(blank=True)
    body = RichTextField(blank=True)
    preparation = models.TextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("intro"), FieldPanel("body"), FieldPanel("preparation")
    ]


class SacramentEnquiry(models.Model):
    sacrament = models.CharField(max_length=80)
    name = models.CharField(max_length=160)
    email = models.EmailField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sacrament}: {self.name}"
