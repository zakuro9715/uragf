from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import User
from .serializers import UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
