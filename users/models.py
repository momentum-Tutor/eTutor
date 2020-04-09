from django.db import models
from django.contrib.auth.models import AbstractUser
from eTutor.models import Language, Room, Friendship, LikeDislike, TimeZone
# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model



class User(AbstractUser):
    primary_language = models.ForeignKey(to=Language, on_delete=models.CASCADE, related_name='primary_language', blank=True, null=True)
    known_languages = models.ManyToManyField(to=Language, related_name='known_languages')
    wanted_languages = models.ManyToManyField(to=Language, related_name='wanted_languages')
    current_time_zone = models.ForeignKey(to=TimeZone, on_delete=models.CASCADE, related_name='current_time_zone', blank=True, null=True)
    

    @property
    def dislikes(self):
        return LikeDislike.objects.filter(user_two=self, like=False).count

    @property
    def likes(self):
        return LikeDislike.objects.filter(user_two=self, like=True).count