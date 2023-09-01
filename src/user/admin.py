from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "is_premium",
        "is_active",
        "is_superuser",
        "is_deleted",
    )
    list_display_links = ("username",)
    list_filter = (
        "is_premium",
        "is_active",
        "is_deleted",
        "is_superuser",
        "created_at",
    )
    readonly_fields = (
        "created_at",
    )
    search_fields = ("email", "username")
    ordering = ("-created_at",)
    list_per_page = 25
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                    "is_superuser",
                    "google_account_id",
                    "is_google_oauth",
                    "is_active",
                    "is_verified",
                    "is_deleted",
                    "created_at",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
