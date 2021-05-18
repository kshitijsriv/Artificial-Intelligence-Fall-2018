# import numpy as np
import manhattan as m

class grid:
    def __init__(self, state, action, g, n):
        self.state = state[:]
        self.action = action[:]
        self.n = n
        self.g = g
        self.h = m.calcManhattan(state, self.n)
        self.f = self.g + self.h
        # return self.state
