"""Get players on an event"""
from django.db import IntegrityError
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from api.models import Player, Event
from api.serializers import PlayerSerializer


class PlayerViewSet(generics.GenericAPIView):
    def get_queryset(self):
        return Player.objects.all()

    def get_serializer_class(self):
        return PlayerSerializer

    def get(self, request, slug, username=None):
        if not username:
            players = Player.objects.filter(event__slug=slug)
        else:
            players = Player.objects.filter(event__slug=slug, username=username)
        x = PlayerSerializer(data=players, many=True)
        x.is_valid()

        if isinstance(x.data, list) and len(x.data) == 1:
            return Response(x.data[0])

        return Response(x.data)

    def post(self, request, slug, username):
        try:
            event = Event.objects.get(slug=slug)
        except Event.DoesNotExist:
            raise ValidationError

        try:
            player = Player.objects.create(event=event, username=username)
            player.save()
        except IntegrityError:
            raise ValidationError

        return Response(status=status.HTTP_201_CREATED)
