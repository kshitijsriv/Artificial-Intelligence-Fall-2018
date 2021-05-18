import time

import minimax as mnmx


# print("WELCOME TO TIC TAC TOE")
# print("Board Layout :")
#
board = list([])
for i in range(9):
    board.append(i+1)
# mnmx.print_board(board)
board = mnmx.clear_board(board)


# start_time = time.time()
while len(mnmx.avail_moves(board)) > 0 and not mnmx.game_done(board):
    board = mnmx.mortal_move(board)
    mnmx.print_board(board)
    board = mnmx.sophia_move(board)
    if len(mnmx.avail_moves(board)) != 0:
        print("SOPHIA'S MOVE")
        mnmx.print_board(board)
    else:
        break

if mnmx.check_winning(board, 'x'):
    print('YOU WIN!')
elif mnmx.check_winning(board, 'o'):
    print('YOU LOSE!')
else:
    print('DRAW!')

exit()
