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
    new = models.BooleanField(default=False)
    accepted_notification = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='accepted_notification', null=True, blank=True)

    def __str__(self):
        return f'{self.user_one.username} and {self.user_two.username}'

class Notifications(models.Model):
    video = models.PositiveIntegerField(default=0)
    dm = models.PositiveIntegerField(default=0)
    friend = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='notification', null=True, blank=True)

    def __str__(self):
        return self.user.username

class LikeDislike(models.Model):
    user_one = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='user_ones', null=True, blank=True)
    user_two = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='user_twos', null=True, blank=True)
    like = models.BooleanField(default=True)


class TimeZone(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Room_Users(models.Model):
    user_one = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='room_user_one', null=True, blank=True)
    user_two = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='room_user_two', null=True, blank=True)
    dm = models.ForeignKey(to='Room', on_delete=models.CASCADE, related_name='room_users', null=True, blank=True)

    def __str__(self):
        return f"users: {self.user_one}, {self.user_two}"

class DM_Notifications(models.Model):
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, related_name='dm_notification', null=True, blank=True)
    new = models.BooleanField(default=False)
    user = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='user_dm_notification', null=True, blank=True)