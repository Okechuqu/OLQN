from django.conf import settings
from django.db import models


class StaffProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.user.get_username()
