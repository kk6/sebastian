from django.urls import path

from . import views

urlpatterns = [
    path("", views.CommuteListView.as_view(), name="commute_list"),
    path("register/", views.register_commutes, name="register_commutes"),
    path("<int:pk>/edit/", views.CommuteUpdateView.as_view(), name="edit_commutes"),
]
