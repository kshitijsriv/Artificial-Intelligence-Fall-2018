import neighbors as ng


def test(state, n):
    for element in state:
        neighbor = ng.findneighbors(element, n)
        nbr = len(neighbor)

        for i in list(range(nbr)):
            if state[element] == state[neighbor[i]]:
                return False

    return True
