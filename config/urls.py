from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from eTutor import views as etutor_views
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', etutor_views.homePage, name="homepage"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('users/', etutor_views.usersPage, name="all_users"),
    path('rooms/', etutor_views.all_rooms, name="all_rooms"),
    path('rooms/<slug:slug>', etutor_views.room_detail),
    path('videoChat/', etutor_views.video_chat, name="video_chat"),
    url(r'token$', etutor_views.token, name="token"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
