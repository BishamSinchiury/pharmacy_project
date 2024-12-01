from django.shortcuts import render
from rest_framework.permissions import BasePermission

# Create your views here.
class IsManagerPermission(BasePermission):
    """
    Custom permission to only allow access to admins.
    """
    def has_permission(self, request, view):
        # Get the user from the request (the user is added to the request object after authentication)
        user = request.user
        
        # Check if the user has the `is_admin` claim set to `True`
        if user.is_manager:
            return True
        return False

 
class IsStaffPermission(BasePermission):
    """
    Custom permission to only allow access to staffs.
    """
    def has_permission(self, request, view):
        # Get the user from the request (the user is added to the request object after authentication)
        user = request.user
        
        # Check if the user has the `is_admin` claim set to `True`
        if user.is_staff:
            return True
        return False
    

