import resource

import goalTest as gt
import moves
import gridpuzzle as gp


def performAStar(input1):
    state = [int(i) for i in input1]
    l = len(state)
    n = int(l**0.5)
    goal = list(range(l))
    count = 0
    start = gp.grid(state, ["start"], 0, n)

    frontier = set()
    explored = set()

    frontier.add(start)

    while len(frontier) != 0:
        count += 1
        state1 = min(frontier, key= lambda x: x.f)
        frontier.remove(state1)
        s = state1.state
        a = state1.action
        print("Current State : %s" % s)
        smcost = state1.g

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

            if ind not in [int(i) for i in range(n)]:
                t1 = a[:]
                t1.append("up")
                temp = gp.grid(moves.up(s, n), t1, smcost + 1, n)
                frontier.add(temp)

            if ind not in [int(i) for i in range(l - n, l)]:
                t1 = a[:]
                t1.append("down")
                temp = gp.grid(moves.down(s, n), t1, smcost + 1, n)
                frontier.add(temp)

            if ind not in [int(i) for i in range(0, l - n + 1, n)]:
                t1 = a[:]
                t1.append("left")
                temp = gp.grid(moves.left(s, n), t1, smcost + 1, n)
                frontier.add(temp)

            if ind not in [int(i) for i in range(n - 1, l, n)]:
                t1 = a[:]
                t1.append("right")
                temp = gp.grid(moves.right(s, n), t1, smcost + 1, n)
                frontier.add(temp)

    print("Solution not found")
    exit(1)
