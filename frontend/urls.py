from django.conf.urls import url
from .views import template as t

urlpatterns = [
    url(r'^rooms/$', t('rooms/room_list.html')),
    url(r'', t('index.html')),
]
