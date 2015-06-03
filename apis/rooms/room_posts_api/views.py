from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView

from posts.models import Post
from posts.serializers import PostSerializer

from rooms.views import RoomMixin

from apis.rooms_api.permissions import JoiningUserOnly


class PostList(ListCreateAPIView, RoomMixin):
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        JoiningUserOnly
    )

    def perform_create(self, serializer):
        serializer.save(room=self.get_room(), user=self.request.user)

    def get_queryset(self):
        filters = {'room': self.get_room()}
        from_date = self.get_from_date()
        if from_date:
            filters['date_created__gte'] = from_date
        return Post.objects.filter(**filters).all()

    def get_from_date(self):
        from django.utils.dateparse import parse_datetime
        from_str = self.request.GET.get('from', False)
        if from_str:
            try:
                return parse_datetime(from_str)
            except ValueError:
                return None
