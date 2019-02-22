from rest_framework.permissions import BasePermission

class IsThisMarketManager(BasePermission):
    
    def has_permission(self, request, view):
        print(request.data)
        return request.user == request.user

