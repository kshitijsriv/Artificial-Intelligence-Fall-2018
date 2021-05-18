def up(state, n):
    now_state = state[:]
    i = now_state.index(0)
    now_state[i], now_state[i-n] = now_state[i-n], now_state[i]
    return now_state

def down(state, n):
    now_state = state[:]
    i = now_state.index(0)
    now_state[i], now_state[i+n] = now_state[i+n], now_state[i]
    return now_state

def left(state, n):
    now_state = state[:]
    i = now_state.index(0)
    now_state[i], now_state[i-1] = now_state[i-1], now_state[i]
    return now_state

def right(state, n):
    now_state = state[:]
    i = now_state.index(0)
    now_state[i], now_state[i+1] = now_state[i+1], now_state[i]
    return now_state