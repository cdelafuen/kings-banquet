from __future__ import unicode_literals

import random

from django.db import models


class CardListField(models.TextField):
    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(CardListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_prep_value(self, value):
        if not value:
            return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)


class Game(models.Model):

    # datetime = models.DateTimeField(auto_now_add=True)
    # turn_player_cards = CardListField()
    # turn_king_cards = CardListField()
    # turn_discard_pile = CardListField()
    # turn_players = CardListField()
    # active_player = models.PositiveSmallIntegerField(default=0)

    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(*args, **kwargs)
        self.player_cards = []
        self.king_cards = []
        self.discard_pile = []
        self.players = []
        self.active_player = 0

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

    def start_new_turn(self):
        turn_cards = []
        for player in self.players:
            if not player.active_card:
                turn_cards.append(player.get_new_active_card())
        king_card = self.draw_king_card()
        return turn_cards, king_card

    def end_new_turn(self, turn_cards, king_card):
        # Return (or not) the active card for each player
        for index, turn_card in enumerate(turn_cards, start=0):
            if turn_card:  # TODO add draw or not rule, now discard by default
                self.players[index].add_card(turn_card)
            self.players[index].active_card = None
            if self.players[index].check_win():
                raise WinError(self.players[index])
        # Get new active player
        self.active_player = (self.active_player + 1) % len(self.players)
        # Return the king_card if its not empty
        if king_card:
            self.add_king_card(king_card)


class WinError(Exception):
    """
    Someone has won
    """
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

    def check_win(self):
        if not self.card_pile and not self.active_card:
            return True
        return False
