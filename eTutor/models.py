from django.db import models
from users.models import User

class Messaging(models.Model):
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='message_sender')
    recipient = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='message_recipient')
    message = models.TextField(null=True, blank=True)


