from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):#this is custom permission now use it in the viewset class.
    def has_permission(self, request, view):
        if request.method is permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    
class FullDjangoModelPermissions(permissions.DjangoModelPermissions):
    def __init__(self) -> None:
        super().perms_map['GET']=['%(app_label)s.view _%(model_name)s']
        #we change add to view.

class ViewCustomerHistoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # implementation here is slightly different from above
        return request.user.has_perm('store.view_history')
        # if it return ture the user will see the history. 