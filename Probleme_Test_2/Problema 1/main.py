import numpy as np

N = 5
CONFLICT = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
]

'''
Functia fitness
'''
def fitness(indiv):
    nrConflicte = 0
    for i in range(len(indiv) - 1):
        if CONFLICT[int(indiv[i])][int(indiv[i + 1])] == 1:
            nrConflicte += 1
    return 1 / (nrConflicte + 1)

'''
Populatia initiala
'''
def generare_populatie_initiala(dim):
    pop = []
    for _ in range(dim):
        indiv = np.random.permutation(N)
        fit = fitness(indiv)
        indiv = np.append(indiv, fit)
        pop.append(indiv)
    return pop

'''
Selectia parintilor prin turnir
'''
def turnir(pop, k):
    pop_turnir = []
    for _ in range(k):
        index = np.random.randint(0, len(pop))
        pop_turnir.append(pop[index])
    fitnesses = [indiv[-1] for indiv in pop_turnir]
    index_castigator = np.argmax(fitnesses)
    return pop_turnir[index_castigator]

def selectia_parintilor(pop, k):
    pop_parinti = []
    for _ in range(len(pop)):
        indiv_castigator = turnir(pop, k)
        pop_parinti.append(indiv_castigator)
    return pop_parinti

'''
Generarea copiilor
'''
def recombinare_parinti(pop):
    pop_copii = pop.copy()
    for i in range(0, len(pop), 2):
        if i + 1 < len(pop):
            indiv1 = pop[i][:-1]
            indiv2 = pop[i + 1][:-1]
            index1, index2 = sorted(np.random.choice(len(indiv1), 2, replace=False))

            copil1 = indiv1.copy()
            copil1[index1:index2] = indiv2[index1:index2]
            copil2 = indiv2.copy()
            copil2[index1:index2] = indiv1[index1:index2]

            copil1_fit = fitness(copil1)
            copil2_fit = fitness(copil2)
            copil1 = np.append(copil1, copil1_fit)
            copil2 = np.append(copil2, copil2_fit)

            pop_copii[i] = copil1
            pop_copii[i + 1] = copil2
    return pop_copii

'''
Mutatie prin inversiune
'''
def mutatie(pop, prob_mut):
    pop_mutanti = []
    for indiv in pop:
        indiv_nou = indiv[:-1].copy()
        if np.random.uniform(0, 1) < prob_mut:
            index1, index2 = np.random.choice(len(indiv_nou), 2, replace=False)
            indiv_nou[index1], indiv_nou[index2] = indiv_nou[index2], indiv_nou[index1]

        fit = fitness(indiv_nou)
        indiv_nou = np.append(indiv_nou, fit)
        pop_mutanti.append(indiv_nou)
    return pop_mutanti

'''
GA
'''
MAX_GENERATIONS = 3
NO_IMPROVEMENT_LIMIT = 3

def algoritm(dim, k):
    populatia = generare_populatie_initiala(dim)
    best_fitness = 0
    best_individual = None
    generatii_fara_imbunatatire = 0
    current_generation = 0

    while current_generation < MAX_GENERATIONS and generatii_fara_imbunatatire < NO_IMPROVEMENT_LIMIT:
        populatia_parinti = selectia_parintilor(populatia, k)
        populatia_copii = recombinare_parinti(populatia_parinti)
        populatia_mutanta = mutatie(populatia_copii, 0.2)

        populatia = populatia_mutanta
        current_best = max(populatia, key=lambda indiv: indiv[-1])

        if current_best[-1] > best_fitness:
            best_fitness = current_best[-1]
            best_individual = current_best
            generatii_fara_imbunatatire = 0
        else:
            generatii_fara_imbunatatire += 1

        current_generation += 1

        print(f"Generatia {current_generation}: Fitness: {best_fitness}")

    print("Cel mai bun individ final:")
    print(best_individual)
    print("Fitness-ul sau:")
    print(best_fitness)

'''
Apelarea algoritmului
'''
algoritm(50, 5)
