from django.db import models

# Create your models here.


class Card(models.Model):

    image = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    cal = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        abstract = True


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

    def __unicode__(self):
        return u'{pk} {name}'.format(pk=self.pk, name=self.name)


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
