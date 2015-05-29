from rest_framework import permissions


class JoiningUserOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.get_room().is_user_joining(request.user)
