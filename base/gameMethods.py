from base.MaxNAI import get_possible_moves, make_a_move, maxN
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
    

