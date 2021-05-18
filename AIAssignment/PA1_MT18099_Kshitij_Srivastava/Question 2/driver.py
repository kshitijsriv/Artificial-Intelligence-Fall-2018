import bfs
import dfs
import time

input1 = input("Enter grid\n").split(' ')
start_time1 = time.time()
print("\nBFS Output:")
print("================================================================")
bfs.performBFS(input1)
print("Time consumed = %s seconds" % (time.time() - start_time1))
start_time2 = time.time()
print("\nDFS Output:")
print("================================================================")
dfs.performDFS(input1)
print("Time consumed = %s seconds" % (time.time() - start_time2))