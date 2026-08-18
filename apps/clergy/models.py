from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string
from wagtail.snippets.models import register_snippet


@register_snippet
class ClergyMember(models.Model):
    name = models.CharField(max_length=160)
    role = models.CharField(max_length=120)
    biography = models.TextField(blank=True)
    photo = models.ForeignKey(
        get_image_model_string(), null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    display_order = models.PositiveSmallIntegerField(default=0)
    panels = [
        FieldPanel("name"), FieldPanel("role"), FieldPanel("biography"),
        FieldPanel("photo"), FieldPanel("display_order"),
    ]

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name
