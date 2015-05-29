from django.conf.urls import url

from posts.views import PostList

urlpatterns = [
    url(r'^(?P<room_id>\d+)/posts/', PostList.as_view()),
]
