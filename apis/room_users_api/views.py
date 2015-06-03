from rest_framework.generics import ListAPIView
from users.serializers import UserSerializer
from rooms.views import RoomMixin


class UserList(ListAPIView, RoomMixin):
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.get_room().users.all()
