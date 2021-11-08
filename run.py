from simulate.sim import gunfight
from initialize.generation import initialise_match


def run():
    match = initialise_match()
    map_status = match.map.assemble_board()

    player_1 = match.team_1.players[0]
    player_2 = match.team_2.players[0]

    gunfight(player_1, player_2)

    pass


run()
