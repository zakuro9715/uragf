from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from accounts.permissions import IsOwnerOrReadOnly

from .serializers import UserSerializer
from .models import User


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )
