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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    states = []
    successors = Stack()
    successors.push((problem.getStartState(), 0, 0))

    crossedStates = []

    while (1):
        current = successors.pop()

        if not current[0] in crossedStates:
            crossedStates.append(current[0])
            states.append(current)
            if problem.isGoalState(current[0]):
                break
            newSuccessors = problem.getSuccessors(current[0])
            if len(newSuccessors) > 0:
                for item in newSuccessors:
                    successors.push(item)
            else:
                states.pop(-1)


    return map(lambda item: item[1], states[1:])

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    # Fila de sucessores que contera somente os nodos nao percorridos
    successors = Queue()
    # O pai eh adicionado a tupla dos nodos
    successors.push((problem.getStartState(), 0, 0, None))

    # Lista para verificar se o nodo ja foi percorrido em algum momento
    crossedStates = []

    # O estado final que sera utilizado para encontrar o caminho percorrido
    final_state = None

    while (not final_state):
        current = successors.pop()
        if(not current[0] in crossedStates):
            if problem.isGoalState(current[0]):
                final_state = current
            else:
                crossedStates.append(current[0])
                for successor in problem.getSuccessors(current[0]):
                    successors.push(successor + (current,))

    # O caminho percorrido para chegar ao estado final
    final_path = []
    while(final_state[3] != None):
        final_path.insert(0, final_state[1])
        final_state = final_state[3]
    return final_path


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

