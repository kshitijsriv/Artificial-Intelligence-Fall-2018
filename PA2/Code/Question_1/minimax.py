import time


def check_winning(board, player):
    if ((board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)):

        return True
    else:
        return False


def avail_moves(board):
    empty = list([])
    for i in range(len(board)):
        if board[i] != 'o' and board[i] != 'x':
            empty.append(i)

    return empty


def check_termination_score(board):
    if check_winning(board, 'x'):
        return -1
    elif check_winning(board, 'o'):
        return +1
    else:
        return 0


def minmax(board, depth, player):
    # c += 1
    if player == 'o':
        best = [-1, -1000]
    else:
        best = [-1, 1000]
    if depth == 0 or game_done(board):
        score = check_termination_score(board)
        return [-1, score]
    for i in avail_moves(board):
        move = i
        board[move] = player
        if player == 'x':
            score = minmax(board, depth - 1, 'o')
        else:
            score = minmax(board, depth - 1, 'x')
        board[move] = " "
        score[0] = move
        if player == 'o':
            if score[1] > best[1]:
                best = score
        else:
            if score[1] < best[1]:
                best = score
    return best


def print_board(board):
    for i in range(3):
        for j in range(3):
            print(str('|') + str(board[(3*i) + j]) + str('|'), end="")
        print("\n---------")


def clear_board(board):
    for i in range(9):
        board[i] = " "
    return board


def game_done(board):
    return check_winning(board, 'x') or check_winning(board, 'o')


def mk_move(board, pos, c):
    board[pos] = c
    return board


def mortal_move(board):
    h_move = input("Play your move : ")
    h_move = int(h_move)
    h_move -= 1
    return mk_move(board, h_move, 'x')


def sophia_move(board):
    start_time = time.time()
    depth = len(avail_moves(board))
    if depth == 0 or game_done(board):
        return board

    move = minmax(board, depth, 'o')
    # print("MOVE TUPLE ========== ", move)
    pos = move[0]
    # print("MOVE SCORE = ", move[1])
    # print("Number of states = ", move[2])
    print("Time taken to make this move = %s seconds" % (time.time() - start_time))

    return mk_move(board, pos, 'o')
