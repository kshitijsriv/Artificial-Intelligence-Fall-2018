import resource
from collections import deque
import neighbors as ng
import goalTest as gt
import printGrid as pG

def performBFS(input1):
    state = [int(i) for i in input1]
    l = len(state)
    n = int(l ** 0.5)
    count = 0
    openstates = deque()
    closed = set()
    openstates.append(state)

    while openstates is not None:
        count += 1
        state1 = openstates.popleft()
        print("Current State : %s" % state1)
        if gt.test(state1, n):
            print("Solved")
            print("Solution state :")
            pG.prnt(state1, n)
            print("\nNumber of iterations = %d" % count)
            print("Memory used (in Bytes) = %s" % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        else:
            closed.add(tuple(state1))

        for element in list(range(l)):
            neighbors = ng.findneighbors(element, n)
            nbrno = len(neighbors)
            diffneighbors = ng.finddiffneighbors(state1, element, neighbors, nbrno)
            diffnbrno = len(diffneighbors)
            if nbrno != diffnbrno and diffnbrno != 0:
                for i in diffneighbors:
                    swappedState = ng.swapneighbors(state1, element, i)
                    if tuple(swappedState) not in closed:
                        openstates.append(swappedState)

    print("Solution not found")
    exit(1)
