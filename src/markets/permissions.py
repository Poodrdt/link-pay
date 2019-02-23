from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

class IsThisMarketManager(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            if request.user.is_superuser:
                return True
            if request.user.groups.filter(name="MarketManager").first():
                return bool(list(set(obj.markets.all()) & set(request.user.markets.all())))
            return False
        return True

