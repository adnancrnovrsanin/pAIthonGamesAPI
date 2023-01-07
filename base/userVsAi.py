import secrets
from . import MinimaxAI
from . import builder

def getStartingBoard(rows, columns):
    board = builder.mapBuilder(rows, columns)
    startComp = [secrets.randbelow(len(board)), secrets.randbelow(len(board[0]))]
    startUser = [secrets.randbelow(len(board)), secrets.randbelow(len(board[0]))]
    while startComp == startUser:
        startComp = [secrets.randbelow(len(board)), secrets.randbelow(len(board[0]))]
        startUser = [secrets.randbelow(len(board)), secrets.randbelow(len(board[0]))]
    board[startComp[0]][startComp[1]] = '0'
    board[startUser[0]][startUser[1]] = '1'
    return board

def aiMoveController(board):
    if not MinimaxAI.game_is_over(board):
        average = round((len(board) + len(board[0])/2))
        if average < 6:
            depth = 10
        elif average < 12:
            depth = 7
        else:
            depth = 5
        result = MinimaxAI.minimax(board, depth, -float("inf"), float("inf"), "0")
        MinimaxAI.make_a_move(result[1][0], result[1][1], board, result[1][2], result[1][3], "0")
        return board
    else:
        return board

def getWinner(board):
    if MinimaxAI.has_won(board, "0"):
        return "Computer"
    elif MinimaxAI.has_won(board, "1"):
        return "User"
    else:
        return "Draw"