# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In busca.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from lib.searchProblem import SearchProblem

import lib.util as util
from lib.util import Stack, Queue, PriorityQueue
'''
Uso da pilha:
stack = Stack()
stack.push(element)
l = stack.list # Lista de elementos na pilha
e = stack.pop()

Uso da fila:
queue = Queue()
queue.push(element)
l = queue.list # Lista de elementos na fila
e = queue.pop()

Uso da fila de prioridades:
queuep = PriorityQueue()
queuep.push(element, value) # Valores baixos indicam maior prioridade
queuep.update(element, value) # Atualiza o valor de prioridade  de um elemento
l = queuep.heap # Lista de elementos na fila
e = queuep.pop()
'''


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    def nodeAddition(successor, successors, current, problem):
        successors.push(successor + (current,))

    # Pilha de sucessores que sempre removera os nodos mais profundos antes
    successors = Stack()
    # O pai eh adicionado a tupla dos nodos
    successors.push((problem.getStartState(), 0, 0, None))

    return genericSearch(successors, problem, nodeAddition)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    def nodeAddition(successor, successors, current, problem):
        successors.push(successor + (current,))

    # Fila de sucessores que contera somente os nodos nao percorridos
    successors = Queue()
    # O pai eh adicionado a tupla dos nodos
    successors.push((problem.getStartState(), 0, 0, None))

    return genericSearch(successors, problem, nodeAddition)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    def nodeAddition(successor, successors, current, problem):
        weight = successor[2] + current[2]
        successors.push(
            (successor[0], successor[1], weight, current), weight)

    # Fila de sucessores que contera somente os nodos nao percorridos
    successors = PriorityQueue()
    # O pai eh adicionado a tupla dos nodos
    successors.push((problem.getStartState(), 0, 0, None), 0)

    return genericSearch(successors, problem, nodeAddition)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    def nodeAddition(successor, successors, current, problem, heuristic):
        weight = successor[2] + current[2]
        successors.push(
            (successor[0], successor[1], weight, current), weight + heuristic(successor[0], problem))

    # Fila de sucessores que contera somente os nodos nao percorridos
    successors = PriorityQueue()
    # O pai eh adicionado a tupla dos nodos
    successors.push((problem.getStartState(), 0, 0, None),
                    heuristic(problem.getStartState(), problem))

    return genericSearch(successors, problem, nodeAddition, heuristic)


def traverseResultantPath(node):
    """Percorre os pais do **node para encontrar o caminho resultante"""
    finalPath = []
    while(node[3] != None):
        finalPath.insert(0, node[1])
        node = node[3]
    return finalPath


def genericSearch(successors, problem, nodeAddition, heuristic=None):
    """Realiza uma busca generica que recebe uma funcao para definar o que será feito com cada sucessor"""
    # O estado final que sera utilizado para encontrar o caminho percorrido
    finalState = None
    # Lista para verificar se o nodo ja foi percorrido em algum momento
    crossedStates = []

    while (not finalState):
        current = successors.pop()
        # Se ele ainda nao foi percorrido anteriormente
        if(not current[0] in crossedStates):
            # Verifica se eh o nodo final
            if problem.isGoalState(current[0]):
                finalState = current
            else:
                # Senao abre os sucessores e para cada um adiciona a pilha com o pai(nodo atual)
                crossedStates.append(current[0])
                for successor in problem.getSuccessors(current[0]):
                    if heuristic:
                        nodeAddition(successor, successors,
                                     current, problem, heuristic)
                    else:
                        nodeAddition(successor, successors,
                                     current, problem)

    # Percorre o caminho do estado final, percorrendo os pais
    return traverseResultantPath(finalState)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
