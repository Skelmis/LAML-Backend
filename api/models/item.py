from django.db import models

from .player import Player


class Item(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, editable=False)
    amount = models.PositiveSmallIntegerField()
