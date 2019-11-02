from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeForm
from .forms import UserCreationForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    """ユーザーアドミン"""

    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("username", "name", "email")
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("username", "name", "email", "password")}),
        ("Permissions", {"fields": ("is_admin",)}),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


# Register
admin.site.register(User, UserAdmin)

# Unregister
admin.site.unregister(Group)
