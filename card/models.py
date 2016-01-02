from copy import copy

from django.db import models

# Create your models here.


class Card(models.Model):

    image = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    cal = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'{pk} {name}'.format(pk=self.pk, name=self.name)


class PlayerCard(Card):
    FIRST = 'first'
    SECOND = 'second'
    DESSERT = 'dessert'
    DRINK = 'drink'
    ORDER_CHOICES = (
        (FIRST, 'first'),
        (SECOND, 'second'),
        (DESSERT, 'dessert'),
        (DRINK, 'drink')
    )

    SWEET = 'sweet'
    SPICY = 'spicy'
    SALTY = 'salty'
    TASTY = 'tasty'
    FLAVOUR_CHOICES = (
        (SWEET, 'sweet'),
        (SPICY, 'spicy'),
        (SALTY, 'salty'),
        (TASTY, 'tasty')
    )

    order = models.CharField(max_length=45, choices=ORDER_CHOICES, blank=True, null=True)
    flavour = models.CharField(max_length=45, choices=FLAVOUR_CHOICES, blank=True, null=True)


class KingCard(Card):

    BANQUET = 'banquet'
    DIET = 'diet'
    THIRSTY = 'thirsty'
    BIG_ONES = 'big_ones'
    LITTLE_ONES = 'little_ones'
    NOT_ME = 'not_me'
    ACTION_CHOICES = (
        (BANQUET, 'banquet'),
        (DIET, 'diet'),
        (THIRSTY, 'thirsty'),
        (BIG_ONES, 'big_ones'),
        (LITTLE_ONES, 'little_ones'),
        (NOT_ME, 'not_me')
    )

    number_of_firsts = models.PositiveSmallIntegerField(blank=True, null=True)
    number_of_seconds = models.PositiveSmallIntegerField(blank=True, null=True)
    number_of_desserts = models.PositiveSmallIntegerField(blank=True, null=True)
    today_eat = models.CharField(max_length=100, blank=True, null=True)
    action = models.CharField(max_length=45, choices=ACTION_CHOICES, blank=True, null=True)

    def execute_action(self, turn_cards):
        returned_cards = copy(turn_cards)
        if not self.action:
            eaten_calories = 0
            eaten_firsts = 0
            eaten_seconds = 0
            eaten_desserts = 0
            for card in turn_cards:
                check_today_eat = True
                check_first = True
                check_second = True
                check_dessert = True
                check_calories = True
                if self.today_eat:
                    check_today_eat = card.flavour in self.today_eat
                if self.number_of_firsts:
                    if card.order == card.FIRST:
                        check_first = eaten_firsts < self.number_of_firsts
                        eaten_firsts += 1
                if self.number_of_seconds:
                    if card.order == card.SECOND:
                        check_second = eaten_seconds < self.number_of_seconds
                        eaten_seconds += 1
                if self.number_of_desserts:
                    if card.order == card.DESSERT:
                        check_dessert = eaten_desserts < self.number_of_desserts
                        eaten_desserts += 1
                if self.cal:
                    check_calories = (eaten_desserts + card.cal) <= eaten_calories
                    if check_calories:
                        eaten_calories += card.cal
        else:
            # TODO multiple action-functions
            pass

        return turn_cards, returned_cards

    def _execute_banquet(self, cards):
        return [None for card in cards]

    def _execute_diet(self, cards):
        return cards

    def _execute_thirsty(self, cards):
        # TODO think about the 3 cards rule
        returned_cards = []
        for card in cards:
            if card.order and card.order == card.DRINK:
                returned_cards.append(None)
            else:
                returned_cards.append(card)
        return returned_cards

    def _execute_big_ones(self, cards):
        returned_cards = []
        for card in cards:
            if card.cal >= self.cal:
                returned_cards.append(None)
            else:
                returned_cards.append(card)
        return returned_cards

    def _execute_little_ones(self, cards):
        returned_cards = []
        for card in cards:
            if card.cal <= self.cal:
                returned_cards.append(None)
            else:
                returned_cards.append(card)
        return returned_cards

    def _execute_not_me(self, cards):
        return cards
