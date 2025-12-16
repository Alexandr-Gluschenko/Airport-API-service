from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method in SAFE_METHODS:
            return bool(user and user.is_authenticated)
        return bool(user and user.is_staff)


class IsOrderOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsTicketOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.order == request.user
