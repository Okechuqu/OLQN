from django.db import models


class NotificationLog(models.Model):
    recipient = models.CharField(max_length=254)
    template = models.CharField(max_length=120)
    provider_id = models.CharField(max_length=160, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.template}: {self.recipient}"
