import random

from db.models import (
    Loadout,
    Weapon,
    Player,
    Team,
    Match,
    Map,
    WeaponModel,
    MapWithPlayer,
)


def initialise_weapons(weapon_names, weapon_category):
    return [
        WeaponModel(name=wn, category=weapon_category) for wn in weapon_names
    ]


primary_weapons = initialise_weapons(['AK-47', 'MP5', 'Famas', 'RPG'], 1)
secondary_weapons = initialise_weapons(['Shotgun', 'Pistol', 'Launcher'], 2)
melee_weapons = initialise_weapons(['Knife', 'Punch'], 3)
lethal_weapons = initialise_weapons(['Grenade', 'Throwing knife'], 4)


def initialise_loadout():
    # primary = copy.deepcopy(random.choice(primary_weapons))
    primary = random.choice(primary_weapons)
    primary_weapon = Weapon(colour=random.choice([
        'black', 'grey', 'white', 'silver', 'gold'
    ]), model=primary)
    return Loadout(
        primary=primary_weapon,
        secondary=random.choice(secondary_weapons),
        melee=random.choice(melee_weapons),
        lethal=random.choice(lethal_weapons)
    )

map_with_players = []

def initialise_player(number, team_shorthand):

    random_id = ''.join(str(random.randint(0, 9)) for i in range(8))

    player = Player(
        username=f'Player_{random_id}',
        id=int(random_id)
    )

    player.shorthand = f'{ team_shorthand }P{ (number + 1) }'

    player.loadout = initialise_loadout()

    map_with_players.append(MapWithPlayer(player=player))

    return player


def initialise_team(team_name: str, team_shorthand: str):
    players = [initialise_player(p, team_shorthand) for p in range(6)]
    return Team(
        name=team_name,
        players=players,
        shorthand=team_shorthand
    )


def initialise_map():
    map_name = 'Hanger'
    map_columns = 20
    map_rows = 10
    map_starting_positions = [
        [(0, 2), (0, 5), (0, 8), (0, 11), (0, 14), (0, 17)],
        [(9, 2), (9, 5), (9, 8), (9, 11), (9, 14), (9, 17)]
    ]
    return Map(map_name, map_columns, map_rows, map_starting_positions)


def initialise_match():
    match_map = initialise_map()
    match = Match(
        team_1=initialise_team('Team 1', 'T1'),
        team_2=initialise_team('Team 2', 'T2'),
        map=match_map,
    )
    match_map.map_with_players = map_with_players
    return match
