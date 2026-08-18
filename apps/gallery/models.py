from django.db import models
from wagtail.images import get_image_model_string


class GalleryItem(models.Model):
    title = models.CharField(max_length=160)
    image = models.ForeignKey(get_image_model_string(), on_delete=models.CASCADE, related_name="+")
    captured_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
