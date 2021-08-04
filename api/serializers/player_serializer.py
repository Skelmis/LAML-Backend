from django.db.models import Sum
from rest_framework import serializers

from api.models import Player, Item


class PlayerSerializer(serializers.ModelSerializer):
    item_count = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ("username", "item_count")

    def get_item_count(self, obj):
        amount = Item.objects.filter(player=obj).aggregate(Sum("amount"))
        return amount["amount__sum"] or 0
