import numpy as np
import ant_colony as ac
import copy
import plot

n = 40
num_ant = 20
iterations = 200
alpha = 0.75
beta = 10
q = 10
rho = 0.4
x = []
y = []
cities = []
for i in range(n):
    cities.append(i)
    x.append(np.random.randint(0, n + 1000))
    y.append(np.random.randint(0, n + 1000))

x = np.array(x)
y = np.array(y)
dist_matrix = []
eta = []
cities_coordinates = np.array(list(zip(x, y)))
for i in range(n):
    dist_matrix.append([])
    for j in range(n):
        dist_matrix[i].append(ac.distance(cities_coordinates[i], cities_coordinates[j]))
dist_matrix = np.array(dist_matrix)
# print(dist_matrix)

pheromone_matrix = [[1 / (n * n) for j in range(n)] for i in range(n)]
pheromone_matrix = np.array(pheromone_matrix)
for i in range(n):
    eta.append([])
    for j in range(n):
        if dist_matrix[i][j] != 0:
            eta[i].append(1 / dist_matrix[i][j])
        else:
            eta[i].append(0)

eta = np.array(eta)

# best_cost_arr = []
# converge = []
# for i in range(0, 1000, 10):
#     print("NUM_GEN ", i)
# for i in range(5, 45, 5):
best_path, best_path_cost, gen_taken = ac.aco(copy.deepcopy(dist_matrix), pheromone_matrix, eta, cities, n, num_ant, iterations, alpha, beta, q, rho)
# best_cost_arr.append(best_path_cost)
# converge.append(gen_taken)

# ants = []
# rho_arr = []
# alpha = []
# beta = []
# for i in range(5, 45, 5):
#     ants.append(i)

# print(converge)
# print(rho_arr)
# plot.cost_vs_gen(converge, ants)
plot.pyplot_path(n, x, y, dist_matrix, best_path)
#
# generations = []
# print(best_cost_arr)
# for i in range(10, 1010, 10):
#     generations.append(i)
# print(generations)
# print(best_path)
# print(best_path_cost)
# print("LENGTH = ", len(best_path))

# plot.cost_vs_gen(best_cost_arr, generations)
