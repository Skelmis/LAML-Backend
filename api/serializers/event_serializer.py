from rest_framework import serializers

from api.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("slug", "title", "description", "item_type", "item_max")
