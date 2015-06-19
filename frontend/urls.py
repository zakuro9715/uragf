from django.conf.urls import url
from .views import template as t

urlpatterns = [
    url(r'', t('index.html')),
]
