from rest_framework.generics import (
    ListCreateAPIView, get_object_or_404
)

from posts.models import Post
from posts.serializers import PostSerializer

from .models import Room


class PostList(ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        room = get_object_or_404(Room.objects, pk=self.kwargs['pk'])
        return Post.objects.filter(room=room).all()
