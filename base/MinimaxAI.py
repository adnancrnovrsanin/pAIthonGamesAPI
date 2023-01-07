from collections import deque
from copy import deepcopy
from math import sqrt
import random
random.seed(108)

def move_is_valid(board, row, col):
    if row < 0 or row >= len(board):
        return False
    if col < 0 or col >= len(board[0]):
        return False
    if board[row][col] != 'r':
        return False
    return True

def locate_player(board, player):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == player:
                return (row, col)
    return None

def make_a_move(currRow, currCol, board, row, col, player):
    if not move_is_valid(board, row, col):
        return False
    board[currRow][currCol] = 'h'
    if (player == "0"):
        board[row][col] = '0'
    else: 
        board[row][col] = '1'
    return True

def board_is_empty(board):
    for row in board:
        for col in row:
            if col == 'r':
                return False
    return True

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

def game_is_over(board):
    if board_is_empty(board):
        return True
    if len(get_possible_moves(board, '0')) == 0:
        return True
    if len(get_possible_moves(board, '1')) == 0:
        return True
    return False

def distance_from_center(board, row, col):
    return sqrt(pow((col - round(len(board[0])/2)), 2) + pow((row - round(len(board)/2)), 2))

def difference_of_distance_from_center(board):
    maxDistance = 0
    minDistance = 0
    for row in range(0, len(board) - 1):
        for col in range(0, len(board[0]) - 1):
            if board[row][col] == '0':
                maxDistance += distance_from_center(board, row, col)
            if board[row][col] == '1':
                minDistance += distance_from_center(board, row, col)
    return minDistance - maxDistance

def difference_of_moves(board):
    return len(get_possible_moves(board, '0')) - len(get_possible_moves(board, '1'))

def get_next_nodes(board, x, y):
    check_next_node = lambda x, y: move_is_valid(board, x, y)
    ways = [(-1, 0), (+1, 0), (0, -1), (0, +1), (-1, -1), (-1, +1), (+1, -1), (+1, +1)]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]

def bfsSum(startRow, startCol, board):
    graph = {}
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(board, x, y)
    queue = deque([(startRow, startCol, board[startRow][startCol])])
    visited = {(startRow, startCol): None}

    density = 0
    while queue:
        cur_node = queue.popleft()
        if cur_node[2] == 'h':
            continue
        
        if cur_node[2] == 'r':
            density += 1

        next_nodes = graph[(cur_node[0], cur_node[1])]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append((next_node[0], next_node[1], board[next_node[0]][next_node[1]]))
                visited[(next_node[0], next_node[1])] = cur_node
    return density

def check_density(board, player):
    density = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == player:
                density += bfsSum(row, col, board)
    return density

def difference_of_density(board):
    return check_density(board, '0') - check_density(board, '1')

def get_score(board):
    if board_is_empty(board):
        return 0
    if len(get_possible_moves(board, '0')) == 0:
        return -float("inf")
    if len(get_possible_moves(board, '1')) == 0:
        return float("inf")
    return 10*difference_of_density(board) + 25*difference_of_moves(board) + 5*difference_of_distance_from_center(board)

def has_won(board, player):
    if len(get_possible_moves(board, "0")) == 0:
        if (player == "1"):
            return True
        else:
            return False
    if len(get_possible_moves(board, "1")) == 0:
        if (player == "0"):
            return True
        else:
            return False
    return False

def minimax(board, depth, alpha, beta, player):
    if game_is_over(board) or depth == 0:
        return [get_score(board), []]
    if player == "0":
        best_score = -float("inf")
        moves = get_possible_moves(board, "0")
        random.shuffle(moves)
        best_move = moves[0]
        for move in moves:
            currRow, currCol, row, col = move
            new_board = deepcopy(board)
            make_a_move(currRow, currCol, new_board, row, col, "0")
            score = minimax(new_board, (depth - 1), alpha, beta, "1")[0]
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break
        return [best_score, best_move]
    else:
        best_score = float("inf")
        moves = get_possible_moves(board, "1")
        random.shuffle(moves)
        best_move = moves[0]
        for move in moves:
            currRow, currCol, row, col = move
            new_board = deepcopy(board)
            make_a_move(currRow, currCol, new_board, row, col, "1")
            score = minimax(new_board, (depth - 1), alpha, beta, "0")[0]
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, best_score)
            if alpha >= beta:
                break
        return [best_score, best_move]