from collections import deque
from heapq import heappop, heappush

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_next_nodes(x, y, grid):
    check_next_node = lambda x, y: True if 0 <= x < len(grid) and 0 <= y < len(grid[0]) else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1] 
    return [(grid[x + dx][y + dy], (x + dx, y + dy)) for dx, dy in ways if check_next_node(x + dx, y + dy)]

def astar(start, goal, graph):
    queue = []
    heappush(queue, (0, start))
    cost_visited = {start: 0}
    visited = {start: None}

    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            break
        
        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                priority = new_cost + heuristic(neigh_node, goal)
                heappush(queue, (priority, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
    return visited

def getAgentPath(start, goal, grid):

    graph = {}
    for x, row in enumerate(grid):
        # print(y, row)
        for y, col in enumerate(row):
            # print(x, col)
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y, grid)

    visited = astar(start, goal, graph)

    x = goal
    path = []
    while x in visited:
        path.append(list(x))
        x = visited[x]
    path.reverse()
    return path