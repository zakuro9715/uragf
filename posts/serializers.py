from rest_framework import serializers
from posts.models import Post

from users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'user', 'date_created')
        read_only_fields = ('user',)
