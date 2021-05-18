from collections import deque


def findneighbors(element, n):
    nbr = []
    if element not in [int(i) for i in range(n)]:
        nbr.append(element - n)
    if element not in [int(i) for i in range(n**2 - n, n**2)]:
        nbr.append(element + n)
    if element not in [int(i) for i in range(0, n**2 - n + 1, n)]:
        nbr.append(element - 1)
    if element not in [int(i) for i in range(n - 1, n**2, n)]:
        nbr.append(element + 1)
    return nbr






def finddiffneighbors(state, element,neighbors, nbrno):
    diffnbr = []
    for i in list(range(nbrno)):
        if state[element] != state[neighbors[i]]:
            diffnbr.append(neighbors[i])

    return diffnbr


def swapneighbors(state, element, i):
    state[element], state[i] = state[i], state[element]
    return state