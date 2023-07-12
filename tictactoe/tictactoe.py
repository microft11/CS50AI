"""
Tic Tac Toe Player
"""

from copy import deepcopy

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
    define the X is first
    """
    count_x = 0
    count_o = 0
    for h in board:
        for cell in h:
            if cell == X:
                count_x += 1
            if cell == O:
                count_o += 1

    return X if count_x == count_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionss = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actionss.append((i, j))
    return actionss


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = deepcopy(board)
    fill = player(board)
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("infeasible move")
    new_board[i][j] = fill
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != EMPTY:
            return board[i][0]
        if (board[0][i] == board[1][i] == board[2][i]) and board[2][i] != EMPTY:
            return board[0][i]

    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != EMPTY:
        return board[1][1]

    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != EMPTY:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    for h in board:
        for cell in h:
            if cell == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    flag = winner(board)

    if flag == X:
        return 1
    elif flag == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    X: Max
    O: Min
    """
    def max_value(board):
        option_move = ()
        if terminal(board):
            return utility(board), option_move
        else:
            v = -5
            for action in actions(board):
                minval, _ = min_value(result(board, action))
                if minval > v:
                    v = minval
                    option_move = action
            return v, option_move

    def min_value(board):
        option_move = ()
        if terminal(board):
            return utility(board), option_move
        else:
            v = 5
            for action in actions(board):
                maxval, _ = min_value(result(board, action))
                if maxval < v:
                    v = maxval
                    option_move = action
            return v, option_move

    curr_player = player(board)

    if terminal(board):
        return None

    if curr_player == X:
        return max_value(board)

    else:
        return min_value(board)

'''
add for git test
'''