from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL  # "auth.user"


# Create your models here.
class WaitlistEntry(models.Model):
    user = models.ForeignKey(
        User, default=None, null=True, blank=True, on_delete=models.SET_NULL
    )
    email = models.EmailField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
