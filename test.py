from tictactoe import *
import pprint
board = initial_state()
#
# isX = True
# for i in range(len(board)):
#     for j in range(len(board[i])):
#         board[i][j] = X
#         isX = not isX


board[0][0] = O
board[0][1] = X
board[0][2] = O
board[1][0] = O
board[1][1] = X
board[1][2] = O
board[2][0] = X
board[2][1] = O
board[2][2] = X

pprint.pprint(board)
print(utility(board))
