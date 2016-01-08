from django.shortcuts import render

# Create your views here.
from card.models import PlayerCard, KingCard
from game.forms import GameForm
from game.models import Player, Game


def home(request):
    form = GameForm(request.GET)

    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            player1 = Player(cd['player1_name'], cd['player1_weight'])
            player2 = Player(cd['player2_name'], cd['player2_weight'])
            player3 = Player(cd['player3_name'], cd['player3_weight'])
            players = [player1, player2, player3]
            game = Game()
            game.start(PlayerCard.objects.all(), KingCard.objects.all(), players)
            turn_cards, king_card = game.start_new_turn()
            # game.turn_player_cards = game.player_cards,
            # game.turn_king_cards = game.king_cards,
            # game.turn_discard_pile = game.discard_pile,
            # game.turn_players = game.players
            # game.save()
            # request.session['game'] = game.id
            return render(request, 'turn.html', locals())
        else:
            error = "Rellena todos los datos"

    return render(request, 'home.html', locals())
