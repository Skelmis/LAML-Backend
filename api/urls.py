from django.urls import path, include

from api.views import (
    EventViewSet,
    SingleEventViewSet,
    PlayerViewSet,
    ItemViewSet,
)

urlpatterns = [
    path("", EventViewSet.as_view()),
    path("events/", EventViewSet.as_view()),
    path("event/<slug:slug>/", SingleEventViewSet.as_view()),
    path("event/<slug:slug>/players/", PlayerViewSet.as_view()),
    path("event/<slug:slug>/player/<str:username>/", PlayerViewSet.as_view()),
    path("event/<slug:slug>/player/<str:username>/items/", ItemViewSet.as_view()),
    path(
        "event/<slug:slug>/player/<str:username>/item/<int:amount>",
        ItemViewSet.as_view(),
    ),
]
