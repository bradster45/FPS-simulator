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


def check_position_empty(requested_row: int, requested_col: int, board: list):
    """
    INPUTS: requested_row & requested_col, index's of requested position, e.g: 0, 2
    INPUTS: board, the board array of a map: a nested array of rows & cols
    FUNCTION: check if position on board is populated with a player already
    RETURNS: boolean, true if position is empty (not already populated)
    """

    value = board[requested_row][requested_col]
    if value == '':
        return True
    return False


def get_valid_points(current_position: set, board: list):
    """
    INPUTS: current_position, a set of the current position of a player: example: (0, 2)
    INPUTS: board, the board array of a map: a nested array of rows & cols
    FUNCTION: validate which positions on the board a player can move to
    RETURNS: list of valid points that a player can move from their current position
    """

    valid_points = [current_position]

    current_row = current_position[0]
    current_col = current_position[1]

    # get positions 1 either side of current position
    up_row = current_row - 1
    down_row = current_row + 1
    right_col = current_col + 1
    left_col = current_col - 1

    # check if player is on the edge of the board
    can_move_up = (0 <= up_row < len(board))
    can_move_down = (0 <= down_row < len(board))
    can_move_right = (0 <= right_col < len(board[current_row]))
    can_move_left = (0 <= left_col < len(board[current_row]))

    if can_move_up:
        empty = check_position_empty(up_row, current_col, board)
        if empty:
            valid_points.append((up_row, current_col))

    if can_move_up and can_move_right:
        empty = check_position_empty(up_row, right_col, board)
        if empty:
            valid_points.append((up_row, right_col))

    if can_move_right:
        empty = check_position_empty(current_row, right_col, board)
        if empty:
            valid_points.append((current_row, right_col))

    if can_move_right and can_move_down:
        empty = check_position_empty(down_row, right_col, board)
        if empty:
            valid_points.append((down_row, right_col))

    if can_move_down:
        empty = check_position_empty(down_row, current_col, board)
        if empty:
            valid_points.append((down_row, current_col))

    if can_move_down and can_move_left:
        empty = check_position_empty(down_row, left_col, board)
        if empty:
            valid_points.append((down_row, left_col))

    if can_move_left:
        empty = check_position_empty(current_row, left_col, board)
        if empty:
            valid_points.append((current_row, left_col))

    if can_move_left and can_move_up:
        empty = check_position_empty(up_row, left_col, board)
        if empty:
            valid_points.append((up_row, left_col))

    return valid_points
