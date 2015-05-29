from django.conf.urls import url

from . import views

urlpatterns = [
    url('^(?P<pk>\d+)/$', views.PostDetail.as_view()),
]
