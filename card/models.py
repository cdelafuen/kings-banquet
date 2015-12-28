from django.db import models

# Create your models here.


class Card(models.Model):
    def __unicode__(self):
        return u'{pk}'.format(pk=self.pk)


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

    name = models.CharField(max_length=100)
    cal = models.PositiveSmallIntegerField()
    order = models.CharField(max_length=45, choices=ORDER_CHOICES, blank=True, null=True)
    flavour = models.CharField(max_length=45, choices=FLAVOUR_CHOICES, blank=True, null=True)

    def __unicode__(self):
        return u'{pk} {name}'.format(pk=self.pk, name=self.name)
