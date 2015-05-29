from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<slug>[0-9a-zA-Z_-]+)/$', views.Room.as_view()),
    url(r'^$', views.RoomList.as_view()),
]
