from django.conf.urls import url

from . import views

urlpatterns = [
    url('^(?P<pk>\d+)/$', views.UserDetail.as_view()),
]
