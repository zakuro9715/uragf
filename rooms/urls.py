from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/posts/$', views.PostList.as_view()),
]
