import uuid

from django.db import models


class Donation(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PAID = "paid", "Paid"
        FAILED = "failed", "Failed"

    reference = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    donor_name = models.CharField(max_length=160, blank=True)
    email = models.EmailField()
    purpose = models.CharField(max_length=120, default="General offering")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=12, choices=Status.choices, default=Status.PENDING, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} — {self.amount}"
