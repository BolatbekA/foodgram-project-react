from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return any([request.user.is_admin,
                        request.user.is_staff,
                        request.user.is_superuser,
                        request.method in SAFE_METHODS])
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return any([request.user.is_admin,
                        request.user.is_staff,
                        request.user.is_superuser])
        return request.method in SAFE_METHODS
