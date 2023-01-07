from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.agents import *
from base.userVsAi import *
from base.MinimaxAI import *

@api_view(['POST'])
def getAgentPathAki(request):
    data = request.data

    start = (data["start"][0], data["start"][1])
    goal = (data["goal"][0], data["goal"][1])
    grid = data["grid"]

    return Response({ "path": Aki.get_agent_path(start, goal, grid)})

@api_view(['POST'])
def getAgentPathJocke(request):
    data = request.data

    start = (data["start"][0], data["start"][1])
    goal = (data["goal"][0], data["goal"][1])
    grid = data["grid"]

    return Response({ "path": Jocke.get_agent_path(start, goal, grid)})

@api_view(['POST'])
def getAgentPathDraza(request):
    data = request.data

    start = (data["start"][0], data["start"][1])
    goal = (data["goal"][0], data["goal"][1])
    grid = data["grid"]

    return Response({ "path": Draza.get_agent_path(start, goal, grid)})

@api_view(['POST'])
def getAgentPathBole(request):
    data = request.data

    start = (data["start"][0], data["start"][1])
    goal = (data["goal"][0], data["goal"][1])
    grid = data["grid"]

    return Response({ "path": Bole.get_agent_path(start, goal, grid)})

# For pyStolovina
@api_view(['POST'])
def startingBoard(request):
    return Response({'board': getStartingBoard(request.data['rows'], request.data['columns'])})

@api_view(['POST'])
def aiMove(request):
    if not game_is_over(request.data['board']):
        new_board = aiMoveController(request.data['board'])
        winner = getWinner(new_board)
        if winner == "Computer" or winner == "User":
            return Response({
                'board': new_board,
                'winner': winner
            })
        else:
            return Response({ "board": new_board })
    else:
        return Response({
            'board': request.data['board'],
            'winner': getWinner(request.data['board'])
        })