from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.generics import (
    GenericAPIView, ListCreateAPIView, ListAPIView,
    get_object_or_404,
)

from posts.models import Post
from posts.serializers import PostSerializer

from accounts.serializers import UserSerializer

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
        serializer.save(room=self.get_room())


class UserList(ListAPIView, RoomAPIMixin):
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.get_room().users.all()


class UserJoining(GenericAPIView, RoomAPIMixin):
    serializer_class = UserSerializer

    def has_joined(self, user, room):
        return room.users.filter(pk=user.pk).exists()

    def get(self, request, *args, **kwargs):
        if self.has_joined(request.user, self.get_room()):
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise exceptions.NotFound()

    def put(self, request, *args, **kwargs):
        self.get_room().users.add(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, *args, **kwargs):
        if self.has_joined(request.user, self.get_room()):
            self.get_room().users.remove(request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise exceptions.NotFound()
