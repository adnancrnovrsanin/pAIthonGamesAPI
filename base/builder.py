# function that creates a board with roads and holes 
# for given number of rows and columns with a random percentage of the board filled with roads with minimum being 80% and maximum being 90%.
import random
import secrets

def boardBuilder(rows, colums):
    print(rows)
    print(colums)
    random.seed(secrets.token_bytes(16))
    # create a board with rows and columns
    board = [['h' for x in range(colums)] for y in range(rows)]
    # get the number of cells to be filled with roads
    cells = (rows * colums) * random.uniform(0.65, 0.85)
    print(cells)
    # fill the board with roads
    for i in range(int(cells)):
        # get a random row
        row = secrets.randbelow(rows)
        # get a random column
        column = secrets.randbelow(colums)
        while(board[row][column] == 'r'):
            # get a random row
            row = secrets.randbelow(rows)
            # get a random column
            column = secrets.randbelow(colums)
        # add a road to the board
        board[row][column] = 'r'
    # return the board
    return board

def mapBuilderFinal(rows, columns, numberOfPlayers, numberOfMinimaxPlayers, numberOfExpectimaxPlayers, numberOfMaxNPlayers, numberOfUserPlayers, numberOfMinimaxABPlayers):
    # create a list of available players
    availablePlayers = []
    if (numberOfMinimaxPlayers > 0):
        availablePlayers = ["minimax"]
    if (numberOfExpectimaxPlayers > 0):
        availablePlayers.append("expectimax")
    if (numberOfMaxNPlayers > 0):
        availablePlayers.append("maxN")
    if (numberOfUserPlayers > 0):
        availablePlayers.append("user")
    if (numberOfMinimaxABPlayers > 0):
        availablePlayers.append("minimaxAB")
    userPlayers = []
    aiPlayers = []
    algorithmsInUse = {}
    random.seed(secrets.token_bytes(16))
    # create a board with rows and columns
    board = boardBuilder(rows, columns)
    # fill the board with players
    for i in range(numberOfPlayers):
        # get a random row
        row = secrets.randbelow(len(board))
        # get a random column
        column = secrets.randbelow(len(board[0]))
        while(board[row][column] != 'r' or board[row][column] in availablePlayers):
            # get a random row
            row = secrets.randbelow(len(board))
            # get a random column
            column = secrets.randbelow(len(board[0]))
        # check if the cell is a road
        # get a random player
        player = random.choice(availablePlayers)
        # check if the player is minimax
        if player == "minimax":
            # decrement the number of minimax players
            numberOfMinimaxPlayers -= 1
            # add the player to the ai players
            aiPlayers.append(str(i))
            # add the algorithm to the algorithms in use
            algorithmsInUse[str(i)] = "minimax" 
            if numberOfMinimaxPlayers == 0:
                # remove the player from the available players
                availablePlayers.remove("minimax")
        if player == "minimaxAB":
            # decrement the number of minimaxAB players
            numberOfMinimaxABPlayers -= 1
            # add the player to the ai players
            aiPlayers.append(str(i))
            # add the algorithm to the algorithms in use
            algorithmsInUse[str(i)] = "minimaxAB" 
            if numberOfMinimaxABPlayers == 0:
                # remove the player from the available players
                availablePlayers.remove("minimaxAB")
        # check if the player is expectimax
        if player == "expectimax":
            # decrement the number of expectimax players
            numberOfExpectimaxPlayers -= 1
            # add the player to the ai players
            aiPlayers.append(str(i))
            # add the algorithm to the algorithms in use
            algorithmsInUse[str(i)] = "expectimax" 
            if numberOfExpectimaxPlayers == 0:
                # remove the player from the available players
                availablePlayers.remove("expectimax")
        # check if the player is maxN
        if player == "maxN":
            # decrement the number of maxN players
            numberOfMaxNPlayers -= 1
            # add the player to the ai players
            aiPlayers.append(str(i))
            # add the algorithm to the algorithms in use
            algorithmsInUse[str(i)] = "maxN" 
            if numberOfMaxNPlayers == 0:
                # remove the player from the available players
                availablePlayers.remove("maxN")
        # check if the player is user
        if player == "user":
            # decrement the number of user players
            numberOfUserPlayers -= 1
            # add the player to the user players
            userPlayers.append(str(i))
            if numberOfUserPlayers == 0:
                # remove the player from the available players
                availablePlayers.remove("user")
        # add the player to the board
        board[row][column] = str(i)

    # return dictionary with the board, the user players, the ai players and the algorithms in use
    return {"board": board, "userPlayers": userPlayers, "aiPlayers": aiPlayers, "algorithmsInUse": algorithmsInUse}
            
            