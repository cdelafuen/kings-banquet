from __future__ import unicode_literals

import random

from django.db import models


class Game(models.Model):

    datetime = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(*args, **kwargs)
        self.player_cards = []
        self.king_cards = []
        self.discard_pile = []
        self.players = []

    def start(self, player_cards, king_cards, players):
        """"
        Start the game with the bunch of necessary information and shuffle it
        """
        for player_card in player_cards:
            self.player_cards.append(player_card)
        for king_card in king_cards:
            self.king_cards.append(king_card)
        for player in players:

            self.players.append(player)
        self.players = sorted(players, key=lambda player: player.weight, reverse=True)  # order by weight
        self.shuffle(player_cards=True, king_cards=True)

        cards_to_hand_out = len(self.player_cards) // len(players)
        for turn in range(0, cards_to_hand_out):
            for player in self.players:
                player.add_card(self.draw_player_card())
        self.discard_pile = self.player_cards
        self.player_cards = []

    def shuffle(self, player_cards=False, king_cards=False, discard_pile=False):
        """
        Shuffle the cards
        """
        if player_cards:
            random.shuffle(self.player_cards)
        if king_cards:
            random.shuffle(self.king_cards)
        if discard_pile:
            random.shuffle(self.discard_pile)

    def add_player_card(self, player_card):
        self.player_cards.append(player_card)

    def draw_player_card(self):
        try:
            return self.player_cards.pop(0)
        except IndexError:
            print "Error: no more player cards"

    def add_king_card(self, king_card):
        self.king_cards.append(king_card)

    def draw_king_card(self):
        try:
            return self.king_cards.pop(0)
        except IndexError:
            print "Error: no more king cards"

    def add_discard(self, discard_card):
        self.discard_pile.append(discard_card)

    def draw_from_discard_pile(self):
        try:
            return self.discard_pile.pop(0)
        except IndexError:
            return None


class WinError(Exception):
    pass


class Player(models.Model):

    def __init__(self, name, weight, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.name = name
        self.weight = weight
        self.card_pile = []
        self.active_card = None
        self.not_me_cards = []

    def __unicode__(self):
        return u'{} {}'.format(self.name, self.weight)

    def get_new_active_card(self):
        try:
            self.active_card = self.card_pile.pop(0)
        except IndexError:
            raise WinError(" Player {} won".format(self.name))
        return self.active_card

    def add_card(self, card):
        self.card_pile.append(card)
