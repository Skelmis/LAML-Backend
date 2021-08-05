from django.urls import path, include

from api.views import (
    EventViewSet,
    PlayerViewSet,
    ItemViewSet,
    sitemap_view,
)

urlpatterns = [
    path("", sitemap_view),
    path("events/", EventViewSet.as_view()),
    path("event/<slug:slug>/", EventViewSet.as_view()),
    path("event/<slug:slug>/players/", PlayerViewSet.as_view()),
    path("event/<slug:slug>/player/<str:username>/", PlayerViewSet.as_view()),
    path("event/<slug:slug>/player/<str:username>/items/", ItemViewSet.as_view()),
    path(
        "event/<slug:slug>/player/<str:username>/item/<int:amount>",
        ItemViewSet.as_view(),
    ),
]
