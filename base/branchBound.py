from copy import deepcopy

def get_next_nodes(x, y, grid):
    check_next_node = lambda x, y: True if 0 <= x < len(grid) and 0 <= y < len(grid[0]) else False
    ways = [-1, 0], [0, 1], [1, 0], [0, -1]
    return [(grid[x + dx][y + dy], (x + dx, y + dy)) for dx, dy in ways if check_next_node(x + dx, y + dy)]

def branchBound(start, goal, graph, grid):
    paths = [
        {
            "path": [start],
            "price": grid[start[0]][start[1]]
        }
    ]

    while paths:
        path = paths.pop(0)
        node = path["path"][-1]

        filteredPaths = []
        for dict in paths:
            tempNode = dict["path"][-1]
            if node != tempNode:
                filteredPaths.append(dict)

        paths = filteredPaths

        if node == goal:
            return path["path"]

        next_nodes = graph[node]

        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            pathCoordinates = []
            for p in path["path"]:
                pathCoordinates.append(p)
            if neigh_node not in pathCoordinates:
                newPath = deepcopy(path)
                newPath["path"].append(neigh_node)
                newPath["price"] += neigh_cost
                paths.append(newPath)
        
        paths = sorted(paths, key=lambda e: (e["price"], len(e["path"])))

def getAgentPath(start, goal, grid):
    graph = {}
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y, grid)
    
    return branchBound(start, goal, graph, grid)

