
from base.MaxNAI import maxN
from base.MinimaxAI import expectimax, minimax, minimaxAB


def getLoosers(board):
    loosers = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            try:
                tmp = int(board[row][col])
                tmp2 = get_possible_moves(board, board[row][col])
                if len(tmp2) == 0:
                    loosers.append(board[row][col])
            except:
                continue
    return loosers

def locate_player(board, player):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == player:
                return (row, col)
    return None

def get_possible_moves(board, player):
    moves = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == player:
                if move_is_valid(board, row-1, col):
                    moves.append((row, col, row-1, col))
                if move_is_valid(board, row+1, col):
                    moves.append((row, col, row+1, col))
                if move_is_valid(board, row, col-1):
                    moves.append((row, col, row, col-1))
                if move_is_valid(board, row, col+1):
                    moves.append((row, col, row, col+1))
                if move_is_valid(board, row-1, col-1):
                    moves.append((row, col, row-1, col-1))
                if move_is_valid(board, row-1, col+1):
                    moves.append((row, col, row-1, col+1))
                if move_is_valid(board, row+1, col-1):
                    moves.append((row, col, row+1, col-1))
                if move_is_valid(board, row+1, col+1):
                    moves.append((row, col, row+1, col+1))
    return moves

def board_is_empty(board):
    for row in board:
        for col in row:
            if col == 'r':
                return False
    return True

def move_is_valid(board, row, col):
    if row < 0 or row >= len(board):
        return False
    if col < 0 or col >= len(board[0]):
        return False
    if board[row][col] != 'r':
        return False
    return True

def make_a_move(currRow, currCol, board, row, col, player):
    if not move_is_valid(board, row, col):
        return False
    board[currRow][currCol] = 'h'
    board[row][col] = player
    return True

def get_all_players(board):
    players = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            try:
                tmp = int(board[row][col])
                players.append(board[row][col])
            except:
                continue
    return players

def game_is_over(board):
    # flag that tells us if there was already a player with
    # possible moves on the board
    second = False
    if board_is_empty(board):
        return True
    for player in get_all_players(board):
        row, col = locate_player(board, player)
        if len(get_possible_moves(board, board[row][col])) > 0:
            if second:
                return False
            else:
                second = True
    return True

def aiMoveController(board, aiPlayer, algorithmInUse, depth, time_to_think):
    if algorithmInUse == "minimax":
        move = minimax(board, depth, aiPlayer, aiPlayer)[1]
    if algorithmInUse == "minimaxab":
        move = minimaxAB(board, depth, -float("Inf"), float("Inf"), aiPlayer, aiPlayer)[1]
    elif algorithmInUse == "expectimax":
        move = expectimax(board, depth, aiPlayer, aiPlayer)[1]
    elif algorithmInUse == "maxn":
        move = maxN(board, aiPlayer, depth)[1]
    print(move)
    make_a_move(move[0], move[1], board, move[2], move[3], aiPlayer)
    return board
    

