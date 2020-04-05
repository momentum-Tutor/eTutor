from django.contrib import admin
from .models import Language, Room, Friendship, LikeDislike



admin.site.register(Language)
admin.site.register(Room)
admin.site.register(Friendship)
admin.site.register(LikeDislike)
