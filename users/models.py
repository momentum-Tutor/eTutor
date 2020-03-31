from django.db import models
from django.contrib.auth.models import AbstractUser
from eTutor.models import Language, Room, Friendship
# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model



class User(AbstractUser):
    primary_language = models.ForeignKey(to=Language, on_delete=models.CASCADE, related_name='primary_language', blank=True, null=True)
    known_languages = models.ManyToManyField(to=Language, related_name='known_languages')
    wanted_languages = models.ManyToManyField(to=Language, related_name='wanted_languages')
    current_time_zone = models.CharField(max_length=100, blank=True, null=True)

