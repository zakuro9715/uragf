from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Post
from .serializers import PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
