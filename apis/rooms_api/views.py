from rest_framework import status, exceptions, permissions
from rest_framework.response import Response
from rest_framework.generics import (
    GenericAPIView, ListCreateAPIView, ListAPIView,
    get_object_or_404,
)

from posts.models import Post
from posts.serializers import PostSerializer

from users.serializers import UserSerializer

from rooms.models import Room

from .permissions import JoiningUserOnly


class RoomAPIMixin:
    def get_room(self):
        if not hasattr(self, 'room'):
            slug = self.kwargs['slug']
            self.room = get_object_or_404(Room.objects, slug=slug)
        return self.room


class PostList(ListCreateAPIView, RoomAPIMixin):
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


class UserList(ListAPIView, RoomAPIMixin):
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.get_room().users.all()


class UserJoining(GenericAPIView, RoomAPIMixin):
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request, *args, **kwargs):
        if self.get_room().is_user_joining(request.user):
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise exceptions.NotFound()

    def put(self, request, *args, **kwargs):
        self.get_room().users.add(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, *args, **kwargs):
        if self.get_room().is_user_joining(request.user):
            self.get_room().users.remove(request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise exceptions.NotFound()
