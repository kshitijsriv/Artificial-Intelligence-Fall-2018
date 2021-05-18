import numpy as np
import copy
import math
import plot


def aco(dist_matrix, pheromone_matrix, eta, cities, num_cities, num_ant, iterations, alpha, beta, q, rho):
    generations = []
    best_cost_gen = []
    converge = []
    for i in range(iterations):
        # print("GENERATION", i)
        generations.append(i)
        best_path_cost = float('inf')
        best_path = []
        for j in range(num_ant):
            path = []
            current = np.random.randint(0, num_cities)
            path.append(current)
            allowed = copy.deepcopy(cities)
            allowed.remove(current)
            delta_pheromone = np.zeros([num_cities, num_cities])

            for k in range(num_cities - 1):
                deno = 0
                for l in allowed:
                    deno += ((pheromone_matrix[current][l] ** alpha) * (eta[current][l] ** beta))

                nextt_city = ant(current, allowed, eta, pheromone_matrix, alpha, beta, deno)
                path.append(nextt_city)
                current = nextt_city
                allowed.remove(nextt_city)

            L_distance = calc_city_distance(dist_matrix, path)

            delta_pheromone += update_delta_pheromone(L_distance, delta_pheromone, q, path)
            if best_path_cost > L_distance:
                best_path_cost = L_distance
                best_path = copy.deepcopy(path)
        pheromone_matrix = rho * pheromone_matrix + delta_pheromone
        best_cost_gen.append(best_path_cost)
        if len(best_cost_gen) >= 2:
            if check_convergence(best_path_cost, best_cost_gen):
                print("CONVERGED AT = ", i)
                break
    return best_path, best_path_cost, i


def ant(current, allowed, eta, pheromone_matrix, alpha, beta, deno):
    probabilities = calc_probabilities(pheromone_matrix, eta, current, alpha, beta, allowed, deno)
    nextt = np.random.choice(allowed, p=probabilities)
    return nextt


def update_delta_pheromone(L_distance, delta_pheromone, q, path):
    for i in range(len(path) - 1):
        current = path[i]
        nextt = path[i + 1]
        delta_pheromone[current][nextt] = q / L_distance
    return delta_pheromone


def calc_probabilities(pheromone_matrix, eta, current, alpha, beta, allowed, deno):
    p = []
    for i in allowed:
        t = pheromone_matrix[current][i]
        n = eta[current][i]
        prob = (t ** alpha * n ** beta) / deno
        p.append(prob)
    return p


def calc_city_distance(dist_matrix, path):
    total_distance = 0
    for i in range(len(path) - 1):
        current = path[i]
        nextt = path[i + 1]
        total_distance += dist_matrix[current][nextt]
    return total_distance


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def check_convergence(cost, cost_arr):
    if cost == cost_arr[-1] and cost == cost_arr[-2]:
        return True
    return False
