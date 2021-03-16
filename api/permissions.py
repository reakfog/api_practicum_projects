from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    '''
    This class is needed to provide access to user manipulations with posts.
    The user must be the author of the post to send requests other than 'GET'.
    '''
    def has_object_permission(self, request, view, obj):
        return(
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user)
