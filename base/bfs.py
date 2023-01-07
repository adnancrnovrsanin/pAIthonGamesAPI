from collections import deque

def sumNeighbours(x, y, grid):
    sum = 0
    count = 0
    check_node = lambda x, y: True if 0 <= x < len(grid) and 0 <= y < len(grid[0]) else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    for dx, dy in ways:
        if check_node(x + dx, y + dy):
            count += 1
            sum += grid[x + dx][y + dy]
    return int(sum / count)

def get_next_nodes(x, y, grid):
    check_next_node = lambda x, y: True if 0 <= x < len(grid) and 0 <= y < len(grid[0]) else False
    ways = [-1, 0], [0, 1], [1, 0], [0, -1]
    return [(sumNeighbours(x, y, grid), (x + dx, y + dy), ways.index([dx, dy])) for dx, dy in ways if check_next_node(x + dx, y + dy)]

def bfs(start, goal, graph, grid):
    queue = deque([(grid[start[0]][start[1]], start, 0)])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = sorted(graph[cur_node[1]], key=lambda e: (e[0], e[2]))
        for next_node in next_nodes:
            neigh_node = next_node[1]

            if neigh_node not in visited:
                queue.append(next_node)
                visited[neigh_node] = cur_node[1]
    return visited

def getAgentPath(start, goal, grid):
    graph = {}
    for x, row in enumerate(grid):
        # print(y, row)
        for y, col in enumerate(row):
            # print(x, col)
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y, grid)
    
    visited = bfs(start, goal, graph, grid)

    x = goal
    path = []
    while x in visited:
        path.append(list(x))
        x = visited[x]
    path.reverse()
    return path
