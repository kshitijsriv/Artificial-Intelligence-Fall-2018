import time

import alphabeta as ab


print("WELCOME TO TIC TAC TOE")
print("Board Layout :")

board = list([])
for i in range(9):
    board.append(i+1)
ab.print_board(board)
board = ab.clear_board(board)

while len(ab.avail_moves(board)) > 0 and not ab.game_done(board):
    board = ab.mortal_move(board)
    ab.print_board(board)
    board = ab.sophia_move(board)
    if len(ab.avail_moves(board)) != 0:
        print("SOPHIA'S MOVE")
        ab.print_board(board)
    else:
        break

if ab.check_winning(board, 'x'):
    print('YOU WIN!')
elif ab.check_winning(board, 'o'):
    print('YOU LOSE!')
else:
    print('DRAW!')

exit()
