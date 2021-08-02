from django.db import models

from .event import Event


class Player(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    username = models.TextField()

    class Meta:
        unique_together = ["event", "username"]
