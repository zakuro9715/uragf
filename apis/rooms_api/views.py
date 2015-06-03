from rest_framework import status, exceptions, permissions
from rest_framework.response import Response
from rest_framework.generics import (GenericAPIView, ListAPIView)

from users.serializers import UserSerializer

from rooms.models import Room
from rooms.serializers import RoomSerializer
from rooms.views import RoomMixin


class RoomList(ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class UserList(ListAPIView, RoomMixin):
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.get_room().users.all()


class UserJoining(GenericAPIView, RoomMixin):
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
