from django.urls import path

from . import views

urlpatterns = [
    path("", views.BookPurchaseListView.as_view(), name="purchase_list"),
    path("purchase/", views.BookPurchaseCreateView.as_view(), name="book_purchase"),
]
