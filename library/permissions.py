# library/permissions.py
from rest_framework.permissions import BasePermission

from rest_framework import permissions

class IsMember(permissions.BasePermission):
    """
    Custom permission to only allow members to access certain views (e.g., book list).
    """

    def has_permission(self, request, view):
        # Only allow members (users without is_staff flag) to view book lists
        if request.user.is_authenticated:
            return True  # Members are allowed to view the book list
        return False


class IsSuperAdmin(BasePermission):
    """
    Custom permission to allow access only to super admins (is_staff=True).
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff
