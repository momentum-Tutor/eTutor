from django.contrib import admin
from .models import Language, Room, Friendship, Notifications, LikeDislike, TimeZone, Room_Users, DM_Notifications

admin.site.register(Language)
admin.site.register(Room)
admin.site.register(Friendship)
admin.site.register(Notifications)
admin.site.register(LikeDislike)
admin.site.register(TimeZone)
admin.site.register(Room_Users)
admin.site.register(DM_Notifications)