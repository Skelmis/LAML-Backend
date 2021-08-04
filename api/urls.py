from django.urls import path, include

from api.views import (
    EventViewSet,
    PlayerViewSet,
    SingleEventViewSet,
    SinglePlayerViewSet,
)

urlpatterns = [
    path("", EventViewSet.as_view()),
    path("event/", EventViewSet.as_view()),
    path("event/<int:pk>/", SingleEventViewSet.as_view()),
    path("player/", PlayerViewSet.as_view()),
    path("player/<int:pk>/", SinglePlayerViewSet.as_view()),
]
