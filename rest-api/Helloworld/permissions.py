from rest_framework import permissions

class IsPostPossessor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only access for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow the creator to modify
        return obj.created_by == request.user
