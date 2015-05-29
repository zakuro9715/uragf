from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/posts/$', views.PostList.as_view()),
    url(r'^(?P<pk>\d+)/users/$', views.UserList.as_view()),
    url(r'^(?P<pk>\d+)/users/joining/$', views.UserJoining.as_view()),
]
