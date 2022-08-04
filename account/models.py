from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomizeUser(AbstractUser):
    work_position = models.CharField(max_length=50, blank=False)
    email_confirmed = models.BooleanField(default=False)
