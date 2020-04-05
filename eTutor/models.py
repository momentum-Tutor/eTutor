from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Room(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    private = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Friendship(models.Model):
    user_one = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='user_one', null=True, blank=True)
    user_two = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='user_two', null=True, blank=True)
    accepted_one = models.BooleanField(default=False)
    accepted_two = models.BooleanField(default=False)
    friends = models.BooleanField(default=False)

class Notifications(models.Model):
    video = models.PositiveIntegerField(default=0)
    dm = models.PositiveIntegerField(default=0)
    friend = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='notification', null=True, blank=True)