from django import forms

from .models import BookPurchase


class BookPurchaseForm(forms.ModelForm):
    class Meta:
        model = BookPurchase
        exclude = ("cover", "user")
