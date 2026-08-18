from django.db import models


class SacramentEnquiry(models.Model):
    sacrament = models.CharField(max_length=80)
    name = models.CharField(max_length=160)
    email = models.EmailField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sacrament}: {self.name}"
