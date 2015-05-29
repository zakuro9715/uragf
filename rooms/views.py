from django.views.generic import TemplateView


class Room(TemplateView):
    template_name = 'rooms/room.html'
