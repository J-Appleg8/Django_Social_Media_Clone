from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    # Homepage View
    path("", views.HomePage.as_view(), name="home"),
]
