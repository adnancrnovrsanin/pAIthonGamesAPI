from collections import deque
from copy import deepcopy
import datetime
from math import sqrt
import random

random.seed(205)

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

def is_winner(board, player):
    if(len(get_possible_moves(board, player)) == 0):
        return False
    players = get_all_players(board)
    players.remove(player)
    return all(len(get_possible_moves(board, p)) == 0 for p in players)

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
    if board_is_empty(board):
        return True
    if (len(getLoosers(board)) >= (len(get_all_players(board)) - 1)):
        return True
    return False

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

def distance_from_center(board, row, col):
    return sqrt(pow((col - round(len(board[0])/2)), 2) + pow((row - round(len(board)/2)), 2))

def difference_of_distance_from_center(board, player):
    difference = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            try:
                tmp = int(board[row][col])
                if board[row][col] == player:
                    difference += distance_from_center(board, row, col)
                else:
                    difference -= distance_from_center(board, row, col)
            except:
                continue
    return difference

def difference_of_moves(board, player):
    difference = 0
    for p in get_all_players(board):
        if p == player:
            difference += len(get_possible_moves(board, p))
        else:
            difference -= len(get_possible_moves(board, p))
    return difference

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

def difference_of_density(board, player):
    difference = 0
    for p in get_all_players(board):
        if p == player:
            difference += check_density(board, p)
        else:
            difference -= check_density(board, p)
    return difference

def get_score(board, player):
    if board_is_empty(board):
        return 0
    if (len(get_possible_moves(board, player)) == 0):
        return -float("inf")
    if (is_winner(board, player)):
        return float("inf")
    return 10*difference_of_distance_from_center(board, player) + 25*difference_of_moves(board, player) + 5*difference_of_density(board, player)

def heuristics(board):
    heuristics = {}
    for player in get_all_players(board):
        heuristics[player] = get_score(board, player)
    return heuristics

def get_best_scores_starting_with(board):
    scores = {}
    for player in get_all_players(board):
        scores[player] = -float("Inf")
    return scores

def get_next_player(board, player):
    all_players = get_all_players(board)
    all_players.sort()
    return all_players[(all_players.index(player) + 1) % len(all_players)]
        
def maxN(board, player, depth, time_to_think, start_time):
    time_difference = datetime.datetime.now() - start_time
    if game_is_over(board) or depth == 0 or len(get_possible_moves(board, player)) == 0 or time_difference.total_seconds() >= time_to_think:
        return [heuristics(board), []]
    best_scores = get_best_scores_starting_with(board)
    moves = get_possible_moves(board, player)
    random.shuffle(moves)
    best_move = moves[0]
    for move in moves:
        currRow, currCol, row, col = move
        new_board = deepcopy(board)
        make_a_move(currRow, currCol, new_board, row, col, player)
        scores = maxN(new_board, get_next_player(new_board, player), (depth - 1), time_to_think, start_time)[0]
        if scores[player] > best_scores[player]:
            best_scores = scores
            best_move = move
    return [best_scores, best_move]


        
        