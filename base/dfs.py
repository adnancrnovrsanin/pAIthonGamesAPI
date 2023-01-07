
def get_next_nodes(x, y, grid):
    check_next_node = lambda x, y: True if 0 <= x < len(grid) and 0 <= y < len(grid[0]) else False
    ways = [-1, 0], [0, 1], [1, 0], [0, -1]
    return [(grid[x + dx][y + dy], (x + dx, y + dy), ways.index([dx, dy])) for dx, dy in ways if check_next_node(x + dx, y + dy)]

def dfs(start, goal, graph):
    stack = []
    stack.append((0, start, 0))
    visited = {start: None}

    while stack:
        cur_node = stack.pop()[1]
        if cur_node == goal:
            break

        next_nodes = sorted(graph[cur_node], key=lambda e: (e[0], e[2]), reverse=True)
        for next_node in next_nodes:
            neigh_node = next_node[1]

            if neigh_node not in visited:
                stack.append(next_node)
                visited[neigh_node] = cur_node
    return visited

def getAgentPath(start, goal, grid):
    graph = {}
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y, grid)

    visited = dfs(start, goal, graph)
    
    x = goal
    path = []
    while x in visited:
        path.append(list(x))
        x = visited[x]
    path.reverse()
    return path
