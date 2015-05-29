from django.db import models


class Post(models.Model):
    text = models.TextField()
    user = models.ForeignKey('users.User', related_name='posts')
    room = models.ForeignKey('rooms.Room', related_name='posts')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
