from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Game(models.Model):

    player_cards = models.ManyToManyField('card.PlayerCard')
    king_cards = models.ManyToManyField('card.KingCard')
    discard_pile = models.ManyToManyField('card.PlayerCard')


class Player(models.Model):
    card_pile = models.ManyToManyField('card.PlayerCard')
    active_card = models.OneToOneField('card.PlayerCard')
    not_me_cards = models.PositiveSmallIntegerField()
