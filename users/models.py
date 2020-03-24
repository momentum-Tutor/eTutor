from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    primary_language = models.ForeignKey()
    known_languages = models.ForeignKey()
    wanted_languages = models.ForeignKey()
    current_time_zone = models.CharField(max)

