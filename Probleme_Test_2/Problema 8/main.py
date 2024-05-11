import numpy as np

def load_distances(file_path):
    return np.loadtxt(file_path)


def calculate_fitness(individual, distances):
    total_distance = distances[0, individual[0]] + distances[individual[-1], 0]
    for i in range(len(individual) - 1):
        total_distance += distances[individual[i], individual[i + 1]]
    return total_distance


def generate_initial_population(pop_size, num_islands, n, distances, max_dist):
    population = []
    while len(population) < pop_size:
        individual = np.random.permutation(num_islands)[:n]
        if calculate_fitness(individual, distances) <= max_dist:
            population.append(individual)
    return population

def tournament_selection(population, k, distances):
    indices = np.random.choice(len(population), k, replace=False)
    tournament = [population[i] for i in indices]
    fitnesses = [calculate_fitness(ind, distances) for ind in tournament]
    winner_index = np.argmax(fitnesses)
    return tournament[winner_index]

def order_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(np.random.choice(range(size), 2, replace=False))
    child = [None] * size
    child[start:end] = parent1[start:end]
    remaining = [item for item in parent2 if item not in child[start:end]]
    child[:start] = remaining[:start]
    child[end:] = remaining[start:]
    return child


def swap_mutation(individual, mutation_rate):
    if np.random.rand() < mutation_rate:
        idx1, idx2 = np.random.choice(range(len(individual)), 2, replace=False)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual


def genetic_algorithm(file_path, pop_size, num_islands, n, max_dist, k, mutation_rate):
    distances = load_distances(file_path)
    population = generate_initial_population(pop_size, num_islands, n, distances, max_dist)
    best_fitness = 0
    best_individual = None
    no_improvement = 0

    for generation in range(k):
        new_population = []
        for _ in range(len(population) // 2):
            parent1 = tournament_selection(population, 5, distances)
            parent2 = tournament_selection(population, 5, distances)
            child1 = order_crossover(parent1, parent2)
            child2 = order_crossover(parent2, parent1)
            child1 = swap_mutation(child1, mutation_rate)
            child2 = swap_mutation(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = sorted(new_population, key=lambda ind: calculate_fitness(ind, distances), reverse=True)[:pop_size]
        current_best_fitness = calculate_fitness(population[0], distances)
        if current_best_fitness > best_fitness:
            best_fitness = current_best_fitness
            best_individual = population[0]
            no_improvement = 0
        else:
            no_improvement += 1

        if no_improvement >= 10:
            break

        print(f"Generation {generation + 1}, Best Fitness: {best_fitness}")

    print("Best individual path:", best_individual)
    print("Best individual fitness:", best_fitness)


genetic_algorithm('distante.txt', 10, 10, 5, 1000, 5, 0.2)
