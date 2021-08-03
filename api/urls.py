from django.urls import path, include

from api.views import EventViewSet, PlayerViewSet

urlpatterns = [
    path("", EventViewSet.as_view()),
    path("event/", EventViewSet.as_view()),
    path("player/", PlayerViewSet.as_view()),
]
