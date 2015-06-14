from django.conf.urls import url
from .views import template as t

urlpatterns = [
    url(r'^rooms/(?P<slug>[0-9a-zA-Z_-]+)/$', t('rooms/room.html')),
    url(r'^rooms/$', t('rooms/room_list.html')),
    url(r'^$', t('home/home.html')),
]
