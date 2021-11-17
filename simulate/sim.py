import random


def gunfight(player_1, player_2):
    """
    INPUTS: player_1 & player_2: Insances of Player() model
    FUNCTION: simulate gunfight between players provided
    RETURNS: set containing randomly selected winner & loser (killer & killed)
    """

    # arrays to use in random.choices
    players = [player_1, player_2]
    players_weights = [player_1.skill, player_2.skill]

    # randomly choose a winner using player skill as weights
    winner = random.choices(
        players, weights=players_weights, k=1
    )[0]

    # set loser as player != winner
    loser = player_1
    if winner.id == player_1.id:
        loser = player_2

    return (winner, loser)
