from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.RoomList.as_view()),
]
