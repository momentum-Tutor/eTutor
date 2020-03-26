from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)

class Room(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return self.name