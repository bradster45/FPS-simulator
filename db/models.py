import random
from threading import Event, Thread
from enum import Enum

from simulate.sim import gunfight, get_valid_points


class WeaponCategory(Enum):
    primary = 1
    secondary = 2
    melee = 3
    lethal = 4


class WeaponModel():
    name = 'default'
    category = WeaponCategory

    def __init__(self, name, category) -> None:
        self.name = name
        self.category = category

    def __str__(self) -> str:
        return self.name


class Weapon():
    colour = str
    model = WeaponModel

    def __init__(self, colour, model) -> None:
        self.colour = colour
        self.model = model

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
    shorthand = 'default'

    def __init__(self, id, username) -> None:
        self.id = id
        self.username = username

        self.skill = random.random()

    def __str__(self) -> str:
        return self.username

    def get_KDR(self, ):
        if self.kills > 0:
            return round((self.kills / self.killed), 2)
        return 0

    def print_leaderboard_stats(self, ):
        print(
            self.username,
            self.kills,
            self.killed,
            self.get_KDR(),
            round(self.skill * 100)
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
        return (
            f'Player {self.killer} killed {self.killed} with a {self.weapon}'
        )


class Team():
    name = 'default'
    players = []
    shorthand = 'default'

    def __init__(self, name, players, shorthand) -> None:
        self.name = name
        self.players = players
        self.shorthand = shorthand

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
        self.players = sorted(
            self.players, key=lambda x: x.kills, reverse=True
        )

    def generate_leaderboard_stats(self, ):
        team_totals = self.team_totals()
        print(
            f'{self.name}, total kills: {team_totals[0]}, '
            f'total deaths: {team_totals[1]}'
        )

        for player in self.players:
            player.print_leaderboard_stats()


class MapWithPlayer():
    current_row = 0
    current_col = 0
    player = Player

    def __init__(self, player):
        self.player = player


class Map():
    name = 'default'
    columns = 0
    rows = 0
    board = []
    starting_positions = []
    map_with_players = []

    def __init__(self, name, cols, rows, starting_positions):
        self.name = name
        self.columns = cols
        self.rows = rows
        self.starting_positions = starting_positions

    def check_starting_position(self, x, y):
        for team_starting_positions in self.starting_positions:
            for position in team_starting_positions:
                if x == position[0] and y == position[1]:
                    return True
        return False

    def assemble_board(self, ):

        players = [p for p in self.map_with_players]

        for x in range(self.rows):
            row = []
            for y in range(self.columns):
                is_starting_position = self.check_starting_position(x, y)
                if is_starting_position:
                    player = players.pop(0)
                    row.append(player)
                    player.current_row = x
                    player.current_col = y
                else:
                    row.append('')
            self.board.append(row)
        return self.board

    def display_board(self, ):
        print('-----------------')
        for row in self.board:
            row_output = ''
            for col in row:
                if col and col != '':
                    row_output += f' { col.player.shorthand } '
                else:
                    row_output += ' ---- '
            print(row_output)

    def move_players(self, ):
        for player in self.map_with_players:

            current_point = (player.current_row, player.current_col)
            valid_move_points = get_valid_points(current_point, self.board)
            move_to = random.choice(valid_move_points)

            self.board[player.current_row][player.current_col] = ''
            self.board[move_to[0]][move_to[1]] = player

            player.current_row = move_to[0]
            player.current_col = move_to[1]


class MatchSettings():
    run_time = (2 * 60)
    max_kills = 100


class Match():
    team_1 = Team
    team_2 = Team

    map = Map

    match_settings = MatchSettings()

    def __init__(self, team_1, team_2, map) -> None:
        self.team_1 = team_1
        self.team_2 = team_2
        self.map = map

    def simulate_match(self, ):

        self.map.assemble_board()

        print('--- MATCH STARTED ---')

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

        print(f'Match on {self.map.name} is ongoing. Leaderboard:')

        for stt in sorted_team_totals:
            stt[1].generate_leaderboard_stats()


class MatchSimulationThread(Thread):
    count = 0
    running_speed = 1.0

    def __init__(self, match):
        Thread.__init__(self)
        self.match = match
        self.stopped = Event()

    def run(self):

        # while loop to re-run code every x seconds unless self.stop() is called
        while not self.stopped.wait(self.running_speed):

            self.match.map.move_players()
            # self.match.show_leaderboard()
            self.match.map.display_board()
            self.count += 1

            if self.count == self.match.match_settings.run_time:
                self.stop()

    def stop(self):
        print('------ IT"S TIME TO GO ------')
        self.stopped.set()
