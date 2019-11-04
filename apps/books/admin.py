from django.contrib import admin

from .models import BookPurchase


class BookPurchaseAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "purchase_at", "has_apply")


# Register
admin.site.register(BookPurchase, BookPurchaseAdmin)
