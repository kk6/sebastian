"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from dashboards.views import IndexView
from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path("", IndexView.as_view(template_name="index.html"), name="index"),
    path("", include("users.urls")),
    path("books/", include("books.urls")),
    path("commutes/", include("commutes.urls")),
    path("dashboard/", include("dashboards.urls")),
    path("admin/", admin.site.urls),
]
