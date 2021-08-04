from django.db import IntegrityError
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from api.models import Player, Event, Item
from api.serializers import ItemSerializer


class ItemViewSet(generics.GenericAPIView):
    def get_queryset(self):
        return Player.objects.all()

    def get_serializer_class(self):
        return ItemSerializer

    def get(self, request, slug, username, amount=None):
        try:
            player = Player.objects.get(username=username)
        except Player.DoesNotExist:
            return ValidationError

        items = Item.objects.filter(player=player)
        x = ItemSerializer(data=items, many=True)
        x.is_valid()

        return Response(x.data)

    def post(self, request, slug, username, amount):
        try:
            player = Player.objects.get(username=username)
        except Player.DoesNotExist:
            return ValidationError

        try:
            item = Item.objects.create(player=player, amount=amount)
            item.save()
        except IntegrityError:
            raise ValidationError

        return Response(status=status.HTTP_201_CREATED)
