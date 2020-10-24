from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions
from api.models import User


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.author == request.user


class IsItselfOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user


class IsLibrarianOrNothing(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    message = "Only librarian have permission to see user info."

    def has_permission(self, request, view):
        return request.user.is_librarian

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_librarian
        
        return request.user.is_librarian


