from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from eTutor import views as etutor_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', etutor_views.homepage, name="homepage"),
    path('rooms/', etutor_views.all_rooms, name="all_rooms"),
    path('rooms/<slug:slug>', etutor_views.room_detail),
    url(r'token$', etutor_views.token, name="token"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
