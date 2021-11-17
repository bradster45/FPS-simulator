import copy
import random

from db.models import (
    Loadout,
    Weapon,
    Player,
    Team,
    Match,
    Map,
)


def initialise_weapons(weapon_names, weapon_category):
    return [
        Weapon(name=wn, category=weapon_category) for wn in weapon_names
    ]


primary_weapons = initialise_weapons(['AK-47'], 1)
secondary_weapons = initialise_weapons(['Shotgun', 'Pistol', 'Launcher'], 2)
melee_weapons = initialise_weapons(['Knife', 'Punch'], 3)
lethal_weapons = initialise_weapons(['Grenade', 'Throwing knife'], 4)


def initialise_loadout():
    primary = copy.deepcopy(random.choice(primary_weapons))
    return Loadout(
        primary=primary,
        secondary=random.choice(secondary_weapons),
        melee=random.choice(melee_weapons),
        lethal=random.choice(lethal_weapons)
    )


def initialise_player():

    random_id = ''.join(str(random.randint(0, 9)) for i in range(8))

    player = Player(
        username=f'Player_{random_id}',
        id=int(random_id)
    )

    player.loadout = initialise_loadout()

    return player


def initialise_team(team_name: str):
    players = [initialise_player() for p in range(6)]
    return Team(
        name=team_name,
        players=players,
    )


def initialise_map():
    return Map('Hanger', 20, 10)


def initialise_match():
    match_map = initialise_map()
    return Match(
        team_1=initialise_team('Team 1'),
        team_2=initialise_team('Team 2'),
        map=match_map,
    )
