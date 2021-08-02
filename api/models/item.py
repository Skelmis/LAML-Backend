from django.db import models

from .player import Player


class Item(models.Model):
    player_username = models.ForeignKey(Player, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
