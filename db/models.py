from enum import Enum


class WeaponCategory(Enum):
    primary = 1
    secondary = 2
    melee = 3
    lethal = 4


class Weapon():
    name = 'default'
    category = WeaponCategory

    def __init__(self, name, category) -> None:
        self.name = name
        self.category = category

    def __str__(self) -> str:
        return self.name


class Loadout():
    primary = Weapon
    secondary = Weapon
    melee = Weapon
    lethal = Weapon

    def __init__(self, primary, secondary, melee, lethal) -> None:
        self.primary = primary
        self.secondary = secondary
        self.melee = melee
        self.lethal = lethal


class Player():
    id = 0
    username = 'default'
    killed = 0
    kills = 0
    loadout = Loadout

    def __init__(self, id, username) -> None:
        self.id = id
        self.username = username

    def __str__(self) -> str:
        return self.username


class PlayerKill():
    killer = Player
    killed = Player

    weapon = Weapon

    def __init__(self, killer, killed, weapon) -> None:
        self.killer = killer
        self.killed = killed

        self.killer.kills += 1
        self.killed.killed += 1

        self.weapon = weapon

    def __str__(self) -> str:
        return f'Player {self.killer} killed {self.killed} with a {self.weapon}'


class Team():
    name = 'default'
    players = []

    def __init__(self, name, players) -> None:
        self.name = name
        self.players = players

    def __str__(self) -> str:
        return f'Team {self.name}'


class Match():
    team_1 = Team
    team_2 = Team

    # def simulate_match():
