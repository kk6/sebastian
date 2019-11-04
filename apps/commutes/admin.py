from django.contrib import admin

from .models import Commute


class CommuteAdmin(admin.ModelAdmin):
    list_display = ("user", "date_of_use", "usage_type", "price", "has_apply")


# Register
admin.site.register(Commute, CommuteAdmin)
