from rest_framework.generics import ListAPIView

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
