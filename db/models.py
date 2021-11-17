from enum import Enum
import random

from simulate.sim import gunfight


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

    def get_weapons(self, ):
        return [self.primary, self.secondary, self.melee, self.lethal]


class Player():
    id = 0
    username = 'default'
    killed = 0
    kills = 0
    loadout = Loadout
    skill = 0

    def __init__(self, id, username) -> None:
        self.id = id
        self.username = username

        self.skill = random.random()

    def __str__(self) -> str:
        return self.username

    def get_KDR(self, ):
        return round((self.kills / self.killed), 2)

    def leaderboard_stats(self, ):
        print(
            self.username,
            self.kills,
            self.killed,
            self.get_KDR(),
            round(self.skill, 2)
        )


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

    def team_totals(self, ):

        total_kills = 0
        total_deaths = 0

        for player in self.players:
            total_kills += player.kills
            total_deaths += player.killed

        return (total_kills, total_deaths)

    def order_players(self, ):
        self.players = sorted(self.players, key=lambda x: x.kills, reverse=True)

    def leaderboard_stats(self, ):
        team_totals = self.team_totals()
        print(f'{self.name}, total kills: {team_totals[0]}, total deaths: {team_totals[1]}')

        for t1p in self.players:
            t1p.leaderboard_stats()


class Map():
    name = 'default'
    columns = 0
    rows = 0

    def __init__(self, name, cols, rows):
        self.name = name
        self.columns = cols
        self.rows = rows

    def assemble_board(self, ):
        board = []
        for x in range(self.rows):
            row = ''
            for y in range(self.columns):
                row = row + ' - '
            board.append(row)
        return board


class Match():
    team_1 = Team
    team_2 = Team

    map = Map

    def __init__(self, team_1, team_2, map) -> None:
        self.team_1 = team_1
        self.team_2 = team_2
        self.map = map

    def simulate_gunfights(self, number):

        for x in range(number):

            player_1 = random.choice(self.team_1.players)
            player_2 = random.choice(self.team_2.players)

            simmed_gunfight = gunfight(player_1, player_2)

            winner = simmed_gunfight[0]
            loser = simmed_gunfight[1]

            weapon = random.choice(winner.loadout.get_weapons())

            PlayerKill(winner, loser, weapon)

    def show_leaderboard(self, ):

        self.team_1.order_players()
        self.team_2.order_players()

        team_1_totals = self.team_1.team_totals()
        team_2_totals = self.team_2.team_totals()

        team_totals = [
            (team_1_totals, self.team_1),
            (team_2_totals, self.team_2),
        ]

        sorted_team_totals = sorted(
            team_totals, key=lambda x: x[0][0], reverse=True
        )

        print(f'Match on {self.map.name} finished. Final leaderboard:')

        for stt in sorted_team_totals:
            stt[1].leaderboard_stats()
