from django.db import models


class PaymentEvent(models.Model):
    reference = models.CharField(max_length=160, unique=True)
    event_type = models.CharField(max_length=80)
    payload = models.JSONField()
    processed_at = models.DateTimeField(null=True, blank=True)
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference
