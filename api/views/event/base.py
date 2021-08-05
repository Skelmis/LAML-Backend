from django.db import IntegrityError
from rest_framework import generics, status, mixins
from rest_framework.response import Response

import api
from api.models import Event
from api.serializers import EventSerializer


class EventViewSet(generics.GenericAPIView):
    throttle_scope = "api"

    def get_queryset(self):
        return Event.objects.all()

    def get_serializer_class(self):
        return EventSerializer

    def get(self, request, slug=None):
        if not slug:
            events = Event.objects.all()
        else:
            events = Event.objects.filter(slug=slug)
        x = EventSerializer(data=events, many=True)
        x.is_valid()

        if isinstance(x.data, list) and len(x.data) == 1:
            return Response(x.data[0])

        return Response(x.data)

    def post(self, request, slug=None):
        if not slug:
            return Response(
                {"detail": "Expected slug as a url argument"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EventSerializer(data=request.data)
        if not serializer.is_valid():
            # Invalid data
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save(slug=slug)
        return Response(status=status.HTTP_201_CREATED)

