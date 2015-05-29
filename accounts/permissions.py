from rest_framework import permissions

from .models import User


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        if isinstance(obj, User):
            return obj == request.user

        owner_attributes = ['owner', 'admin', 'user']
        for attr in owner_attributes:
            owner = getattr(obj, attr, False)
            if owner and owner == request.user:
                return True
        return False
