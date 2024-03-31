"""
Tic Tac Toe Player
"""

import math

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
    # Count how much of "X" and "O"
    Count_X = 0
    Count_O = 0
    # Loop to count X and O
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                Count_X += 1
            elif board[i][j] == "O":
                Count_O += 1
    # Emptry board
    if Count_X == 0 and Count_O == 0:
        return "X"
    elif Count_X <= Count_O:
        return "X"
    else:
        return "O"

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_space = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "X" and board[i][j] != "O":
                empty_space.add((i, j))
    return empty_space

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    import copy
    # Copy the board first
    copied_board = copy.deepcopy(board)

    # Check the action then raise the exception if action is not valid
    if 0 > action[0] or action[0] > 2 or 0 > action[1] or action[1] > 2:
        raise ValueError("Invalid Move")

    # Count how much of "X" and "O"
    Count_X = 0
    Count_O = 0
    # Loop to count X and O
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                Count_X += 1
            elif board[i][j] == "O":
                Count_O += 1
    # Emptry board
    if copied_board[action[0]][action[1]] != None:
        raise ValueError("Invalid board")
    if Count_X == 0 and Count_O == 0:
        copied_board[action[0]][action[1]] = "X"
        return copied_board
    elif Count_X <= Count_O:
        copied_board[action[0]][action[1]] = "X"
        return copied_board
    else:
        copied_board[action[0]][action[1]] = "O"
        return copied_board

    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check "EMPTY
    # Count_EMPTY = 0
    # Check row
    for i in range(len(board)):
        if all(_ == "X" for _ in board[i]):
            return "X"
        elif all(_ == "O" for _ in board[i]):
            return "O"
        # Check column
        for j in range(len(board[i])):
            if all(row[j] == "X" for row in board):
                return "X"
            elif all(row[j] == "O" for row in board):
                return "O"
            # elif board[i][j] == "EMPTY":
                # Count_EMPTY += 1

    # Check diagonals direction
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != None:
        return board[0][0]
    elif (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != None:
        return board[0][2]

    # Tie or still don't have the winner
    # elif Count_EMPTY == 0:
    else:
        return None

    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check "EMPTY
    Count_EMPTY = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                Count_EMPTY += 1
    win = winner(board)

    if win == "X" or win == "O":
        return True
    elif Count_EMPTY == 0:
        return True
    else:
        return False

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Check terminal state
    if terminal(board):
        return None
    # Check for player "X" to find the Max
    elif player(board) == "X":
        # Max Function
        bestValue = float('-inf')
        bestAction = None
        for action in actions(board):
            new_board = result(board, action)
            value = Min_func(new_board)
            if value > bestValue:
                bestValue = value
                bestAction = action
        return bestAction
    # Player "O" to find the Min
    else:
        # Min Function
        bestValue = float('inf')
        bestAction = None
        for action in actions(board):
            new_board = result(board, action)
            value = Max_func(new_board)
            if value < bestValue:
                bestValue = value
                bestAction = action
        return bestAction

    # raise NotImplementedError
# Defind the max function


def Max_func(board):
    v = float('-inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, Min_func(result(board, action)))
    return v

# Define the min function


def Min_func(board):
    v = float('inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, Max_func(result(board, action)))
    return v
