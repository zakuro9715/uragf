from django.conf.urls import url
from .views import Room

urlpatterns = [
    url(r'^(?P<slug>[0-9a-zA-Z_-]+)/$', Room.as_view()),
]
