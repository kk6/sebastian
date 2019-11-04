from django.urls import path

from . import views

urlpatterns = [path("", views.CommuteListView.as_view(), name="commute_list")]
