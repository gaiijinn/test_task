from rest_framework.permissions import SAFE_METHODS, BasePermission


class CustomEventPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.method == "POST":
            if view.action == 'add_user_as_guest':
                return request.user.is_authenticated

        if request.method == "DELETE":
            if view.action == 'remove_user_as_guest':
                return request.user.is_authenticated

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if view.action in ['add_user_as_guest', 'remove_user_as_guest']:
            return request.user.is_authenticated

        return obj.organizer == request.user
