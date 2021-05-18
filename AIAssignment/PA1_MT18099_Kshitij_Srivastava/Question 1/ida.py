import resource
import goalTest as gt
import moves
import gridpuzzle as gp


def performIDA(input1):
    state = [int(i) for i in input1]
    l = len(state)
    n = int(l ** 0.5)
    goal = list(range(l))
    count = 0
    start = gp.grid(state, ["start"], 0, n)
    frontier = set()
    bound = start.f

    while True:
        count += 1
        frontier.add(start)
        mincost = 100000
        while len(frontier) != 0:

            state1 = frontier.pop()
            s = state1.state
            a = state1.action
            print("Current State : %s" % s)
            smcost = state1.g

            if gt.test(goal, s):
                print("Solved")
                print("Moves => %s" % a)
                print("Number of moves = %d" % len(a))
                print("Number of iterations = %d" % count)
                print("Memory used (in Bytes) = %s" % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
                return

            ind = s.index(0)

            if ind not in [int(i) for i in range(n)]:
                t1 = a[:]
                t1.append("up")
                temp = gp.grid(moves.up(s, n), t1, smcost + 1, n)

                if temp.f <= bound:
                    frontier.add(temp)
                elif temp.f < mincost:
                    mincost = temp.f

            if ind not in [int(i) for i in range(l - n, l)]:
                t1 = a[:]
                t1.append("down")
                temp = gp.grid(moves.down(s, n), t1, smcost + 1, n)

                if temp.f <= bound:
                    frontier.add(temp)
                elif temp.f < mincost:
                    mincost = temp.f

            if ind not in [int(i) for i in range(0, l - n + 1, n)]:
                t1 = a[:]
                t1.append("left")
                temp = gp.grid(moves.left(s, n), t1, smcost + 1, n)

                if temp.f <= bound:
                    frontier.add(temp)
                elif temp.f < mincost:
                    mincost = temp.f

            if ind not in [int(i) for i in range(n - 1, l, n)]:
                t1 = a[:]
                t1.append("right")
                temp = gp.grid(moves.right(s, n), t1, smcost + 1, n)
                if temp.f <= bound:
                    frontier.add(temp)
                elif temp.f < mincost:
                    mincost = temp.f
        print(mincost)
        if mincost == 100000:
            print("Solution not found")
            exit(1)
        bound = mincost
