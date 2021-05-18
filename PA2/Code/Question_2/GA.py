import numpy as np
import copy

count_prof = 10
count_courses = 20
count_lecture_halls = 4
number_of_iterations = 50

days = 5
slots = 8

n_slots = 8 * 5 * count_lecture_halls

prof = np.zeros(count_prof, dtype=int)
for i in range(count_prof):
    prof[i] = i + 1

course = np.zeros(count_courses, dtype=int)
for i in range(count_courses):
    course[i] = i + 1

pc = []
for i in range(count_courses):
    pc.append([prof[(i % count_prof)], course[i]])


def generate_gene():
    return [pc[np.random.randint(1, count_courses)], np.random.randint(1, 6), np.random.randint(1, 9),
            np.random.randint(1, count_lecture_halls + 1)]


def generate_one_chromosome():
    slot_entry = list([])
    for i in range(n_slots):
        slot_entry.append(generate_gene())
    return slot_entry


def generate_100_chromosomes():
    chromosomes = []
    for l in range(100):
        chromosomes.append(generate_one_chromosome())

    return chromosomes


def calc_fitness(chromosome):
    fitness = 0
    for i in range(n_slots):
        gene = []
        gene.append(chromosome[i])
        test1 = list([])
        test1.append([gene[0][0][0], gene[0][1], gene[0][2]])
        test2 = list([])
        test2.append([gene[0][1], gene[0][2], gene[0][3]])

        for j in range(i + 1, n_slots):
            sche_slot_test1 = list([])
            sche_slot_test2 = list([])
            sche_slot_test1.append([chromosome[j][0][0], chromosome[j][1], chromosome[j][2]])
            sche_slot_test2.append([chromosome[j][1], chromosome[j][2], chromosome[j][3]])

            if test1 == sche_slot_test1 or test2 == sche_slot_test2:
                fitness += 1
                break

    return fitness


def fitness_value_for_all_chromosomes(chromosomes_100):
    all_fitness_values = []
    for i in range(100):
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
    sorted_chromosomes = all_chromosomes[sorted_fitness_indices]
    return sorted_chromosomes


def select_top(sorted_chromosomes, k):
    top_k = []
    for i in range(k):
        top_k.append(sorted_chromosomes[i])
    return top_k


def crossover_single_point(chromosome1, chromosome2):
    point = np.random.randint(0, n_slots)
    child_chromosome_1 = []
    child_chromosome_2 = []

    for i in range(point):
        child_chromosome_1.append(chromosome1[i])
        child_chromosome_2.append(chromosome2[i])

    for j in range(point, n_slots):
        child_chromosome_1.append(chromosome2[j])
        child_chromosome_2.append(chromosome1[j])

    return [child_chromosome_1, child_chromosome_2]


def create_crossover_population_100(top_k_chromosomes, k):
    crossover_single_point_population = []
    for i in range(k):
        parent_1 = top_k_chromosomes[i]
        for j in range(i + 1, k):
            parent_2 = top_k_chromosomes[j]
            children = []
            children.append(crossover_single_point(parent_1, parent_2))
            crossover_single_point_population.append(children[0][0])
            crossover_single_point_population.append(children[0][1])
        crossover_single_point_population.append(parent_1)
    return crossover_single_point_population


def merge_random_and_crossover_population(random_population, crossover_population):
    merged_population = []
    for i in range(min(len(random_population), len(crossover_population))):
        merged_population.append(random_population[i])
        merged_population.append(crossover_population[i])

    return merged_population


def calc_merged_population_fitness(merged_population):
    fitness_merged_population = []
    for i in range(len(merged_population)):
        fitness_merged_population.append(calc_fitness(merged_population[i]))

    return fitness_merged_population


def sort_merged_population(merged_population, fitness_merged_population):
    merged_population = np.array(merged_population)
    fitness_merged_population = np.array(fitness_merged_population)
    sorted_fitness_merged_population = fitness_merged_population.argsort()
    sorted_merged_population = merged_population[sorted_fitness_merged_population]
    return sorted_merged_population


def select_top_100(sorted_merged_population):
    merged_population_top_100 = []
    for i in range(100):
        merged_population_top_100.append(sorted_merged_population[i])
    return merged_population_top_100


def perform_mutation(chromosome, number_of_genes_to_mutate):
    for i in range(number_of_genes_to_mutate):
        gene_pos = np.random.randint(0, n_slots)
        chromosome[gene_pos] = generate_gene()

    return chromosome


def mutation_population(population):
    number_of_genes_to_mutate = 10
    mutated_population = []
    for i in range(100):
        chromosome = population[i]
        mutated_chromosome = perform_mutation(chromosome, number_of_genes_to_mutate)
        mutated_population.append(mutated_chromosome)
    return mutated_population


def merge_top_k(merged_population, top_k):
    for i in range(10):
        merged_population.append(top_k[i])
    return merged_population


if __name__ == '__main__':
    random_population = generate_100_chromosomes()
    population = copy.deepcopy(random_population)
    top_fitness_array = []
    convergence_array = []
    for i in range(number_of_iterations):
        population_fitness_values_list = np.array(fitness_value_for_all_chromosomes(population))
        sorted_fitness = fitness_value_for_all_chromosomes(population)
        sorted_fitness = np.sort(sorted_fitness, axis=0)
        # print("TOP FITNESS : ", sorted_fitness[0])
        # print(sorted_fitness)
        sorted_population = sort_all_by_fitness_values(population_fitness_values_list, population)
        top_fitness_array.append(sorted_fitness[0])
        if convergence_array:
            if convergence_array[len(convergence_array)-1] == sorted_fitness[0]:
                convergence_array.append(sorted_fitness[0])
            else:
                convergence_array = []
                convergence_array.append(sorted_fitness[0])
        if len(convergence_array) == 10:
            print("SOLUTION ======================================= \n", sorted_population[0])
            print("LENGTH OF SOLUTION ======================================= \n", len(sorted_population[0]))
            print("TOP FITNESS VALUES FOR EACH ITERATION : ", top_fitness_array)
            exit(1)

        top_k_population = select_top(sorted_population, 10)
        crossover_population = create_crossover_population_100(top_k_population, 10)
        merged_population = merge_random_and_crossover_population(population, crossover_population)
        merged_population_fitness = calc_merged_population_fitness(merged_population)
        sorted_merged_population = sort_merged_population(merged_population, merged_population_fitness)
        merged_population_100 = select_top_100(sorted_merged_population)
        mutated_population = mutation_population(merged_population_100)
        mutated_and_top_k_population = merge_top_k(mutated_population, top_k_population)
        mutated_population_fitness = calc_merged_population_fitness(mutated_and_top_k_population)
        sorted_added_mutated_population = sort_merged_population(mutated_and_top_k_population,
                                                                 mutated_population_fitness)
        population = select_top_100(sorted_added_mutated_population)

    print("SOLUTION ======================================= \n", sorted_population[0])
    print("LENGTH OF SOLUTION ======================================= \n", len(sorted_population[0]))
    print("TOP FITNESS VALUES FOR EACH ITERATION : ", top_fitness_array)
