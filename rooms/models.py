from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=256, blank=True)
    users = models.ManyToManyField('accounts.User', related_name='rooms')
