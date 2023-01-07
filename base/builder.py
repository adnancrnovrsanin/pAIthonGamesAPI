# function that creates a map with roads and holes 
# for given number of rows and columns with a random percentage of the map filled with roads with minimum being 80% and maximum being 90%.
import random
import secrets

def mapBuilder(rows, colums):
    random.seed(secrets.token_bytes(16))
    # create a map with rows and columns
    map = [['h' for x in range(colums)] for y in range(rows)]
    # get the number of cells to be filled with roads
    cells = (rows * colums) * random.uniform(0.90, 0.95)
    # fill the map with roads
    for i in range(int(cells)):
        map[random.randint(0, rows - 1)][random.randint(0, colums - 1)] = 'r'
    # return the map
    return map