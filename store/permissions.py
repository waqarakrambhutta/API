from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):#this is custom permission now use it in the viewset class.
    def has_permission(self, request, view):
        if request.method is permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)