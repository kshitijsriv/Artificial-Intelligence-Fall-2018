import astar
import ida
import bfs
import dfs

import time

input1 = input("Enter initial state:\n").split(' ')
start_time1 = time.time()
print("Astar Output:")
print("================================================================")
astar.performAStar(input1)
print("Time consumed = %s seconds" % (time.time() - start_time1))
start_time2 = time.time()
print("\nBFS Output:")
print("================================================================")
bfs.performBFS(input1)
print("Time consumed = %s seconds" % (time.time() - start_time2))
start_time3 = time.time()
print("\nDFS Output:")
print("================================================================")
dfs.performDFS(input1)
print("Time consumed = %s seconds" % (time.time() - start_time3))
start_time4 = time.time()
print("\nIDA* Output:")
print("================================================================")
ida.performIDA(input1)
print("Time consumed = %s seconds" % (time.time() - start_time4))
