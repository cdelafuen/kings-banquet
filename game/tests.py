from django.test import TestCase

# Create your tests here.
from game.models import Game


class GameTests(TestCase):

    def setUp(self):
        self.game = Game()

    def test_add_player_card(self):
        self.game.add_player_card('card')
        self.assertEqual(self.game.player_cards[0], 'card')
