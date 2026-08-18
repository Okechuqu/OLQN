from django.db import models


class StreamChannel(models.Model):
    name = models.CharField(max_length=120)
    url = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
