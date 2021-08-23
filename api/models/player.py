from django.db import models

from .event import Event


class Player(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, editable=False)
    username = models.TextField()
    is_finished = models.BooleanField(default=False)

    class Meta:
        unique_together = ["event", "username"]
