from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<slug>[0-9a-zA-Z-_]+)/joining/$', views.UserJoining.as_view()),
]
