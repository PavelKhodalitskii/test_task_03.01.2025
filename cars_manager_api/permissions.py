from rest_framework import permissions
from django.db.models import ForeignKey
from django.contrib.auth.models import User

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Разрешение на POST, PUT, PATCH, DELETE запросы для владельца object
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        for field in obj._meta.get_fields():
            if isinstance(field, ForeignKey) and field.related_model is User:            
                print(field.name)
                return getattr(obj, field.name).id == request.user.id
            
        return True