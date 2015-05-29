from django.views.generic import TemplateView


class Room(TemplateView):
    template_name = 'rooms/room.html'


class RoomList(TemplateView):
    template_name = 'rooms/room_list.html'
