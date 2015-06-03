from rest_framework.generics import get_object_or_404
from django.views.generic import TemplateView

from .models import Room as RoomModel


class RoomMixin:
    def get_room(self):
        if hasattr(self, 'room'):
            return self.room
        slug = self.kwargs['slug']
        self.room = get_object_or_404(RoomModel.objects, slug=slug)
        return self.room


class Room(TemplateView):
    template_name = 'rooms/room.html'


class RoomList(TemplateView):
    template_name = 'rooms/room_list.html'
