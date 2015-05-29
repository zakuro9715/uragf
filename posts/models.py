from django.db import models


class Post(models.Model):
    text = models.TextField()
    user = models.ForeignKey('users.User', related_name='posts')
    room = models.ForeignKey('rooms.Room', related_name='posts')
