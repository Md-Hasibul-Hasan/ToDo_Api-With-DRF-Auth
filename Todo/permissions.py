from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Object-level permission:
    user শুধু নিজের Todo-ই access করতে পারবে
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
