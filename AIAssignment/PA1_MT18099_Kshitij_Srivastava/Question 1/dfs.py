import goalTest as gt
import moves
import griduninformed as gui
import resource


def performDFS(input1):
    state = []
    for i in input1:
        state.append(int(i))
    l = len(state)
    n = int(l**0.5)
    goal = list(range(l))
    count = 0
    start = gui.grid(state, ["start"])

    frontier = list([])
    frontier.append(start)
    explored = set()

    while len(frontier) != 0:
            count += 1

            state1 = frontier.pop()
            s = state1.state[:]
            a = state1.action[:]
            print("Current State : %s" % s)

            if tuple(s) not in explored:
                if gt.test(goal, s):
                    print("Solved")
                    print("Moves => %s" % a)
                    print("Number of moves = %d" % len(a))
                    print("Number of iterations = %d" % count)
                    print("Memory used (in Bytes) = %s" % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
                    return
                else:
                    explored.add(tuple(s))
                ind = s.index(0)

                if ind not in [int(i) for i in range(n - 1, l, n)]:
                    t1 = a[:]
                    t1.append("right")
                    temp = gui.grid(moves.right(s, n), t1)
                    frontier.append(temp)

                if ind not in [int(i) for i in range(n)]:
                    t1 = a[:]
                    t1.append("up")
                    temp = gui.grid(moves.up(s, n), t1)
                    frontier.append(temp)

                if ind not in [int(i) for i in range(l - n, l)]:
                    t1 = a[:]
                    t1.append("down")
                    temp = gui.grid(moves.down(s, n), t1)
                    frontier.append(temp)

                if ind not in [int(i) for i in range(0, l - n + 1, n)]:
                    t1 = a[:]
                    t1.append("left")
                    temp = gui.grid(moves.left(s, n), t1)
                    frontier.append(temp)

    print("Solution not found")
    exit(1)
