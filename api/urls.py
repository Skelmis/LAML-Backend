from django.urls import path, include

from api.views import EventViewSet

urlpatterns = [path("", EventViewSet.as_view())]
