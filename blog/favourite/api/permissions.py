from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    
    def has_permission(self, request, view):# ilk çalışır
        return request.user and request.user.is_authenticated
    message = "You must be the owner of this object"
    
    def has_object_permission(self, request, view, obj):#koşullar sağlandığında çalışır
        return obj.user == request.user  or request.user.is_superuser