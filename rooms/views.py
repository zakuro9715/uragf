from rest_framework.generics import (
    ListCreateAPIView, get_object_or_404
)

from posts.models import Post
from posts.serializers import PostSerializer

from .models import Room


class RoomAPIMixin:
    def get_room(self):
        if not hasattr(self, 'room'):
            self.room = get_object_or_404(Room.objects, pk=self.kwargs['pk'])
        return self.room


class PostList(ListCreateAPIView, RoomAPIMixin):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(room=self.get_room()).all()

    def perform_create(self, serializer):
        post = Post(**serializer.validated_data)
        post.room = self.get_room()
        post.save()
