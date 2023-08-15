from django.contrib import admin
from api.models import User, Chapter, Card, PurchaseLog
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
            {"fields": ("email","customer_id")},
        ),
        (
            ("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
    )

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_free", "price"]


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ["id", "user"]

    
@admin.register(PurchaseLog)
class PurchaseLogAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "chapter", "price", "created_at"]


