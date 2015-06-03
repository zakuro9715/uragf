from rest_framework import status, exceptions, permissions
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from users.serializers import UserSerializer

from rooms.views import RoomMixin


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
