import numpy as np
import copy

count_prof = 10
count_courses = 20
count_lecture_halls = 4
number_of_iterations = 30

days = 5
slots = 8

n_slots = 8 * 5 * count_lecture_halls

prof = np.zeros(count_prof, dtype=int)
for i in range(count_prof):
    prof[i] = i+1

course = np.zeros(count_courses, dtype=int)
for i in range(count_courses):
    course[i] = i+1

pc = []
for i in range(count_courses):
    pc.append([prof[(i % count_prof)], course[i]])


def generate_gene():
    return [pc[np.random.randint(1, count_courses)], np.random.randint(1, 6), np.random.randint(1, 9), np.random.randint(1, count_lecture_halls+1)]


def generate_one_chromosome():
    slot_entry = list([])
    for i in range(n_slots):
        slot_entry.append(generate_gene())
        # print(slot_entry)
    # print("LENGTH OF ONE CHROMOSOME ++++++++++++++++", len(slot_entry))
    return slot_entry


def calc_fitness(chromosome):
    # print("LENGTH OF CHROMOSOME FOR FITNESS = = = = = ", len(chromosome))
    fitness = 0
    for i in range(n_slots):
        gene = []
        gene.append(chromosome[i])
        # print(gene[0][0][0])
        test1 = list([])
        test1.append([gene[0][0][0], gene[0][1], gene[0][2]])
        test2 = list([])
        test2.append([gene[0][1], gene[0][2], gene[0][3]])

        for j in range(i+1, n_slots):
            sche_slot_test1 = list([])
            sche_slot_test2 = list([])
            # print(j)
            sche_slot_test1.append([chromosome[j][0][0], chromosome[j][1], chromosome[j][2]])
            sche_slot_test2.append([chromosome[j][1], chromosome[j][2], chromosome[j][3]])

            if test1 == sche_slot_test1 or test2 == sche_slot_test2:
                fitness += 1
                break

    return fitness


def get_conflict_position(chromosome):
    for i in range(n_slots):
        gene = []
        gene.append(chromosome[i])
        # print(gene[0][0][0])
        test1 = list([])
        test1.append([gene[0][0][0], gene[0][1], gene[0][2]])
        test2 = list([])
        test2.append([gene[0][1], gene[0][2], gene[0][3]])

        for j in range(i+1, n_slots):
            sche_slot_test1 = list([])
            sche_slot_test2 = list([])
            # print(j)
            sche_slot_test1.append([chromosome[j][0][0], chromosome[j][1], chromosome[j][2]])
            sche_slot_test2.append([chromosome[j][1], chromosome[j][2], chromosome[j][3]])

            if test1 == sche_slot_test1 or test2 == sche_slot_test2:
                return i
    return -1

def fitness_value_for_all_chromosomes(chromosomes_100):
    all_fitness_values = []
    for i in range(len(chromosomes_100)):
        ch = chromosomes_100[i]
        all_fitness_values.append(calc_fitness(ch))

    return all_fitness_values


def sorted_fitness_for_all_population(chromosomes):
    fitness = np.array(fitness_value_for_all_chromosomes(chromosomes))
    return np.sort(fitness, axis=0)


def sort_all_by_fitness_values(all_fitness_values, all_chromosomes):
    all_chromosomes = np.array(all_chromosomes)
    all_fitness_values = np.array(all_fitness_values)
    sorted_fitness_indices = all_fitness_values.argsort()
    # print(sorted_fitness_indices)
    sorted_chromosomes = all_chromosomes[sorted_fitness_indices]
    return sorted_chromosomes


def select_top(sorted_chromosomes, k):
    top_k = []
    for i in range(k):
        top_k.append(sorted_chromosomes[i])
    return top_k


def crossover_single_point(chromosome1, chromosome2):
    point = np.random.randint(0, n_slots)
    # print("POINT OF CROSSOVER", point)
    child_chromosome_1 = []
    child_chromosome_2 = []

    for i in range(point):
        child_chromosome_1.append(chromosome1[i])
        child_chromosome_2.append(chromosome2[i])

    for j in range(point, n_slots):
        child_chromosome_1.append(chromosome2[j])
        child_chromosome_2.append(chromosome1[j])

    # print("LENGTH OF CHILD CHROMOSOME = ", len(child_chromosome_2))
    return [child_chromosome_1, child_chromosome_2]


def create_crossover_population_100(top_k_chromosomes, k):
    crossover_single_point_population = []
    for i in range(k):
        parent_1 = top_k_chromosomes[i]
        for j in range(i+1, k):
            parent_2 = top_k_chromosomes[j]
            children = []
            children.append(crossover_single_point(parent_1, parent_2))
            # print("LENGTH OF CHILDRENNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN", len(children[0]))
            crossover_single_point_population.append(children[0][0])
            crossover_single_point_population.append(children[0][1])
        crossover_single_point_population.append(parent_1)
    # print("LENGTH OF CREATED CROSSOVER =======================", len(crossover_single_point_population))
    return crossover_single_point_population


def improve_chromosome(chromosome):
    copy_chromosome = copy.deepcopy(chromosome)
    fitness = calc_fitness(chromosome)
    new_fitness = 10000
    while new_fitness >= fitness:
        conflict_pos = get_conflict_position(chromosome)
        if conflict_pos == -1:
            break
        copy_chromosome[conflict_pos] = generate_gene()
        new_fitness = calc_fitness(copy_chromosome)
    return copy_chromosome


def improve_population(population):
    for i in range(len(population)):
        chromosome = population[i]
        for j in range(2):
            improved_chromosome = improve_chromosome(chromosome)
            population[i] = improved_chromosome
    return population


if __name__ == '__main__':
    population = []
    top_fitness_array = []
    for i in range(10):
        population.append(generate_one_chromosome())

    for i in range(number_of_iterations):
        improved_random_population = improve_population(population)
        crossover_population = create_crossover_population_100(improved_random_population, 10)
        crossover_population_fitness_values = fitness_value_for_all_chromosomes(crossover_population)
        sorted_crossover_population = sort_all_by_fitness_values(crossover_population_fitness_values, crossover_population)
        sorted_fitness = np.sort(crossover_population_fitness_values, axis=0)
        print("TOP FITNESS : ", sorted_fitness[0])
        # print(sorted_fitness)
        top_fitness_array.append(sorted_fitness[0])
        # if check_convergence(top_fitness_array):
        #     print("SOLUTION ======================================= \n", sorted_crossover_population[0])
        #     print("LENGTH OF SOLUTION ======================================= \n", len(sorted_crossover_population[0]))
        #     break
        sorted_crossover_population_TOP_K = select_top(sorted_crossover_population, 10)
        population = sorted_crossover_population
    print("SOLUTION ======================================= \n", sorted_crossover_population[0])
    print("LENGTH OF SOLUTION ======================================= \n", len(sorted_crossover_population[0]))
    print("TOP FITNESS VALUES FOR EACH ITERATION : ", top_fitness_array)
