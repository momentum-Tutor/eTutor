from django.db import models
from django.contrib.auth.models import AbstractUser
from eTutor.models import Language
# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    primary_language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING,)
    known_languages = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING)
    wanted_languages = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING)
    current_time_zone = models.CharField(max_length=100)

