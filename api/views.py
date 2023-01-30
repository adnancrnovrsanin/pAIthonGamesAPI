from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.MaxNAI import *
from base.agents import *
from base.builder import mapBuilderFinal
from base.gameMethods import *

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
    return Response(mapBuilderFinal(
        request.data['rows'],
        request.data['columns'],
        request.data['numberOfPlayers'],
        request.data['numberOfMinimaxPlayers'],
        request.data['numberOfExpectimaxPlayers'],
        request.data['numberOfMaxNPlayers'],
        request.data['numberOfUserPlayers'],
    ))

@api_view(['POST'])
def aiMove(request):
    if not game_is_over(request.data['board']):
        new_board = aiMoveController(
            request.data['board'],
            request.data['aiPlayer'],
            request.data['algorithmInUse'],
            request.data['depth'],
            request.data['time_to_think']
        )
        return Response({
            'board': new_board,
            'loosers': getLoosers(new_board)
        })
    else:
        return Response({
            'board': request.data['board'],
            'loosers': getLoosers(request.data['board'])
        })
    # return Response({
    #     "proba": heuristics(request.data['board'])
    # })