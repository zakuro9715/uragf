from django.db import models


class Post(models.Model):
    text = models.TextField()
    user = models.ForeignKey('accounts.User', related_name='posts')
    room = models.ForeignKey('rooms.Room', related_name='posts')
