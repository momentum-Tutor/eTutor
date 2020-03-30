from django.contrib import admin

from .models import Language, Room, Friendship

admin.site.register(Language)
admin.site.register(Room)
admin.site.register(Friendship)