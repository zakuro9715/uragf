from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.RoomList.as_view()),
    url(r'^(?P<slug>[0-9a-zA-Z-_]+)/posts/$', views.PostList.as_view()),
    url(r'^(?P<slug>[0-9a-zA-Z-_]+)/users/$', views.UserList.as_view()),
    url(r'^(?P<slug>[0-9a-zA-Z-_]+)/joining/$', views.UserJoining.as_view()),
]
