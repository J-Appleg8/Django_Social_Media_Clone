from os import name
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomePage.as_view(), name="home"),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("test/", views.TestPage.as_view(), name="test"),
    path("thanks/", views.ThanksPage.as_view(), name="thanks"),
    path("posts/", include("posts.urls", namespace="posts")),
    path("groups/", include("groups.urls", namespace="groups")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
