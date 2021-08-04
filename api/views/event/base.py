from django.db import IntegrityError
from rest_framework import generics, status, mixins
from rest_framework.response import Response

import api
from api.models import Event
from api.serializers import EventSerializer


class EventViewSet(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class SingleEventViewSet(
    api.UpdateIntegrityCheck, generics.RetrieveUpdateDestroyAPIView
):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "slug"


"""
class EventViewSet(generics.GenericAPIView, mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        #Create and store a new event in the database
        serializer = EventSerializer(data=request.data)
        if not serializer.is_valid():
            # Invalid data
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
"""
