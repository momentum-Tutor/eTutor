from django.db import models
from django.contrib.auth.models import AbstractUser
# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model

class Language(models.Model):
    name = models.CharField(max_length=50)


class User(AbstractUser):
    primary_language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='primary_language', blank=True, null=True)
    known_languages = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='known_languages', blank=True, null=True)
    wanted_languages = models.ForeignKey(to=Language,on_delete=models.DO_NOTHING, related_name='wanted_languages',blank=True, null=True)
    current_time_zone = models.CharField(max_length=100)

