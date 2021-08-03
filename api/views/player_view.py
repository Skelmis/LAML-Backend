from rest_framework import generics

from api.models import Player
from api.serializers import PlayerSerializer


class PlayerViewSet(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
