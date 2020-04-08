from eTutor.models import DM_Notifications
from users.models import User
from django import template

register = template.Library()

@register.filter(name='notifications_for_user')
def notifications_for_user(notification, user):
    if notification.user == user and notification.new is True:
        return 'New'
    else:
        return ''