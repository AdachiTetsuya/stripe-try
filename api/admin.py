from django.contrib import admin
from api.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["id", "username", "email", "is_staff"]
    list_filter = []
    ordering = []
    filter_horizontal = []
    fieldsets = (
        (
            None,
            {"fields": ("email",)},
        ),
        (
            ("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
    )
