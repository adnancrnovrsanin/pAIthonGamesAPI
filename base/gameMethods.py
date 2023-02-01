import datetime
from base.MaxNAI import get_possible_moves, make_a_move, maxN
from base.MinimaxAI import expectimax, minimax, minimaxAB

def getLoosers(board):
    loosers = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            try:
                tmp = int(board[row][col])
                if len(get_possible_moves(board, board[row][col])) == 0:
                    loosers.append(board[row][col])
            except:
                continue
    return loosers

def board_is_empty(board):
    for row in board:
        for col in row:
            if col == 'r':
                return False
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
    if board_is_empty(board):
        return True
    if (len(getLoosers(board)) >= (len(get_all_players(board)) - 1)):
        return True
    return False

def aiMoveController(board, aiPlayer, algorithmInUse, depth, time_to_think):
    if algorithmInUse == "minimax":
        move = minimax(board, depth, aiPlayer, aiPlayer, time_to_think, datetime.datetime.now())[1]
    if algorithmInUse == "minimaxAB":
        move = minimaxAB(board, depth, -float("Inf"), float("Inf"), aiPlayer, True, time_to_think, datetime.datetime.now())[1]
    elif algorithmInUse == "expectimax":
        move = expectimax(board, depth, aiPlayer, True, time_to_think, datetime.datetime.now())[1]
    elif algorithmInUse == "maxN":
        move = maxN(board, aiPlayer, depth, time_to_think, datetime.datetime.now())[1]
    make_a_move(move[0], move[1], board, move[2], move[3], aiPlayer)
    return board
    

