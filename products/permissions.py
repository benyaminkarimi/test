from rest_framework import permissions

class customPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return bool(request.user and request.user.is_staff) 
            
        else:
            return True

class superuserOrCreator(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, product_obj):
        return product_obj.user.id == request.user.id or request.user.is_superuser

                                                                                                