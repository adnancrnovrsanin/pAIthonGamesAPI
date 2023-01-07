from base import astar, bfs, branchBound, dfs


class Aki(object):
    @staticmethod
    def get_agent_path(start, goal, grid):
        return dfs.getAgentPath(start, goal, grid)

class Jocke(object):
    @staticmethod
    def get_agent_path(start, goal, grid):
        return bfs.getAgentPath(start, goal, grid)

class Draza(object):
    @staticmethod
    def get_agent_path(start, goal, grid):
        return branchBound.getAgentPath(start, goal, grid)

class Bole(object):
    @staticmethod
    def get_agent_path(start, goal, grid):
        return astar.getAgentPath(start, goal, grid)



