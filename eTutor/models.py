from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Room(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Friendship(models.Model):
    requester = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='f_requester')
    reciever = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='f_reciever')
    accepted = models.BooleanField(default=False)
    pass