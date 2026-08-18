from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string
from wagtail.models import Page


class GalleryItem(models.Model):
    title = models.CharField(max_length=160)
    image = models.ForeignKey(get_image_model_string(), on_delete=models.CASCADE, related_name="+")
    captured_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class GalleryPage(Page):
    template = "gallery/gallery_page.html"
    intro = models.TextField(blank=True)
    max_count = 1
    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["items"] = GalleryItem.objects.all().select_related("image")
        return context
