"""
Tic Tac Toe Player
"""

from math import inf
from copy import deepcopy
from random import shuffle

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """

    if terminal(board):
        return None

    Xs = 0
    Os = 0
    for row in board:
        for cell in row:
            if cell == X:
                Xs += 1
            elif cell == O:
                Os += 1

    return X if Xs <= Os else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    availableActions = set()
    for i,row in enumerate(board):
        for j,col in enumerate(row):
            if col == EMPTY:
                availableActions.add((i,j))

    return availableActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = deepcopy(board)
    p = player(newBoard)
    i, j = action
    if newBoard[i][j] != EMPTY:
        raise Exception("Invailed Action")

    newBoard[i][j] = p

    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def winningIndexs():
        for row in range(3):
            yield [(row,col) for col in range(3)]

        for col in range(3):
            yield [(row,col) for row in range(3)]
        yield [(i, i) for i in range(3)]
        yield [(i, 3 - 1 - i) for i in range(3)]

    for index in winningIndexs():
        firstI,firstJ = index[0]
        player = board[firstI][firstJ]
        if player == EMPTY:
            continue
        if all(board[i][j] == player for i,j in index):
            return player
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    results = { X: 1,
                O: -1,
                None: 0}

    return results[win]


def minimax(board):
    global alpha, beta
    """
    Returns the optimal action for the current player on the board.
    """

    def score(board, isMax):
        if terminal(board):
            return utility(board)

        possibleActions = list(actions(board))
        shuffle(possibleActions) # to prevent AI from making same moves every time

        compareFunction = max if isMax else min

        bestScore = -inf if isMax else inf
        for action in possibleActions:
            actionScore = score(result(board, action), not isMax)
            bestScore = compareFunction(bestScore, actionScore)


        return bestScore

    possibleActions = list(actions(board))
    shuffle(possibleActions)

    isMax = True if player(board) == O else False
    compareFunction = min if isMax else max

    bestScore = inf if isMax else -inf
    bestMove = (0,0)
    for action in possibleActions:
        actionScore = score(result(board, action), isMax)
        bestScore,bestMove = compareFunction((bestScore,bestMove), (actionScore, action), key=lambda x:x[0])

    return bestMove
