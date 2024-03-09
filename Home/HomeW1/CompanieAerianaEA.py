#Compania Aeriana -> EA
import random

def initialize_population(pop_size):
    population = []
    for _ in range(pop_size):
        while True:
            a = random.randint(0, 50)  
            b = random.randint(0, 83) 
            c = random.randint(0, 100)
            if a * 100 + b * 60 + c * 50 <= 5000:
                population.append([a, b, c])
                break
    return population

def calculate_fitness(individual):
    prices = [100, 60, 50]
    autonomies = [6000, 4200, 2800]
    radar_ranges = [30, 48, 32]
    total_cost = sum(individual[i] * prices[i] for i in range(3))
    total_autonomy = sum(individual[i] * autonomies[i] for i in range(3))
    total_radar_range = sum(individual[i] * radar_ranges[i] for i in range(3))

    num_planes = sum(individual)
    
    fitness = 0 
    if num_planes > 0:
        avg_autonomy = total_autonomy / num_planes
        avg_radar_range = total_radar_range / num_planes
        if avg_radar_range > 40:
            fitness = avg_autonomy
    
    return individual + [fitness]

population = initialize_population(pop_size=50)
population_with_fitness = [calculate_fitness(individual) for individual in population]

for individual_with_fitness in population_with_fitness:
    print(individual_with_fitness)
