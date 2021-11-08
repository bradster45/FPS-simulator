from initialize.generation import (
    initialise_weapons, initialise_team
)
from db.models import (
    Weapon,
    Player,
    PlayerKill,
    Team,
    Match,
)


def run():
    team_1 = initialise_team('Team 1')
    team_2 = initialise_team('Team 2')

    pass


run()
