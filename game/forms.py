# django imports
from django.forms import Form, CharField, IntegerField


class GameForm(Form):

    player1_name = CharField(max_length=100)
    player1_weight = IntegerField()
    player2_name = CharField(max_length=100)
    player2_weight = IntegerField()
    player3_name = CharField(max_length=100)
    player3_weight = IntegerField()
