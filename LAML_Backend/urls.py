from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="LAML API",
        default_version="v1",
        description="A basic API backend for Look At My Leaderboard.\n\nPlease note all routes are ratelimited at "
        "`30/minute`",
        terms_of_service="https://koldfusion.xyz/",
        contact=openapi.Contact(email="ethan@koldfusion.xyz"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(
        r"^doc(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api/auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", include("api.urls")),
    # path("", include("base.urls")),
]
