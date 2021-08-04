from django.db import models

from .player import Player


class Item(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, editable=False)
    amount = models.PositiveSmallIntegerField()
    time_created = models.DateTimeField(auto_now_add=True, editable=False)
