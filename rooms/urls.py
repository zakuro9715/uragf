from django.conf.urls import url
from .views import Room

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', Room.as_view()),
]
