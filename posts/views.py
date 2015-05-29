from rest_framework.exceptions import NotFound
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from rooms.models import Room

from .models import Post
from .serializers import PostSerializer


class PostList(ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        if not Room.objects.filter(id=self.kwargs['room_id']).exists():
            raise NotFound()
        return Post.objects.filter(room=self.kwargs['room_id']).all()


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
