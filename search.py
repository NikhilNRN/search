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
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #Written by Nikhil
    #Variable to keep track of nodes.
    x = util.Stack()
    #List used for tracking visited nodes
    visitedNodes = []
    #Setting initial state to 1 for activation.
    x.push((problem.getStartState(), [], 1))
    #Loops is used here to check if the goal has been met.
    while not x.isEmpty():
        node = x.pop()
        state = node[0]
        operationDone = node[1]
        if problem.isGoalState(state):
            return operationDone
        if state not in visitedNodes:
            visitedNodes.append(state)
            successors = problem.getSuccessors(state)
            for item in successors:
                childState = item[0]
                childOperationDone = item[1]
                if childState not in visitedNodes:
                    childAction = operationDone + [childOperationDone]
                    x.push((childState, childAction, 1))
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #Same setup as depth first search. Only difference is I used a Queue here.
    # Written by Nikhil
    x = util.Queue()
    visitedNode = []
    x.push((problem.getStartState(), [], 1))
    while not x.isEmpty():
        node = x.pop()
        state = node[0]
        operationDone = node[1]
        if problem.isGoalState(state):
            return operationDone
        if state not in visitedNode:
            visitedNode.append(state)
            success = problem.getSuccessors(state)
            for item in success:
                childState = item[0]
                childOperationDone = item[1]
                if childState not in visitedNode:
                    childAction = operationDone + [childOperationDone]
                    x.push((childState, childAction, 1))
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #Written by Nikhil
    #Initialized all variables and queues for cost function.
    pacmanQueue = util.PriorityQueue()
    state = set()
    x = (problem.getStartState(), 0, [])
    pacmanQueue.push(x, 0)
    #While queue is not empty, we are moving the pacman based on the direction and cost.
    while not pacmanQueue.isEmpty():
        (node1, cost, direction) = pacmanQueue.pop()
        if problem.isGoalState(node1):
            return direction
        if not node1 in state:
            state.add(node1)
            for nextNode, nextOperation, nextCost in problem.getSuccessors(node1):
                directionTotal = direction + [nextOperation]
                costTotal = cost + nextCost
                stateTotal = (nextNode, costTotal, directionTotal)
                pacmanQueue.push(stateTotal, costTotal)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    #Written by Andrew
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue() #creates a priority queue to store the frontier nodes
    nodesVisited = [] #creates an array to store the nodes that were visited
    actionsList = [] #creates array to store actions
    
    frontier.push((problem.getStartState(), actionsList), heuristic(problem.getStartState(), problem))
    
    while frontier:
        node, action = frontier.pop()
        
        if not node in nodesVisited:
            nodesVisited.append(node)
            if problem.isGoalState(node):
                return action
            for successor in problem.getSuccessors(node):
                location, direction, cost = successor
                nextActions = action + [direction]
                nextCost = problem.getCostOfActions(nextActions) + heuristic(location, problem)
                frontier.push((location, nextActions), nextCost)
    return []

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
