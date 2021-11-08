import random

from db.models import (
    PlayerKill
)


def gunfight(player_1, player_2):
    shuffle = random.shuffle([player_1, player_2])

    winner = shuffle[0]
    loser = shuffle[1]

    PlayerKill(winner, loser, winner)
