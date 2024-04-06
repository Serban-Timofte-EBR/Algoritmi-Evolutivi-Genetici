import numpy

def fitness(indiv):
    nr_gene = len(indiv)
    fitness = 0
    for i in range(nr_gene - 1):
        for j in range(i + 1, nr_gene):
            if abs(indiv[i] - indiv[j]) == abs(i - j):
                fitness += 1

    return nr_gene * ((nr_gene - 1)/2) - fitness

def generare_populatie_initiala(dim, n):
    population = []
    for i in range(dim):
        indiv = numpy.random.permutation(n)
        fit = fitness(indiv)
        indiv = list(indiv)
        indiv.append(fit)
        population.append(indiv)
    return population

pop1 = generare_populatie_initiala(5, 5)
print(pop1)

def noua_generatie(pop, k):
    pop2 = []

    # SALVAM CEL MAI BUN INDIVID
    fitS = [indiv[-1] for indiv in pop]
    valMax = numpy.argmax(fitS)
    bestIndiv = pop[valMax]
    pop2.append(bestIndiv)

    while len(pop2) < len(pop):
        popTurnir = []
        indexuriTurnir = numpy.random.choice(len(pop), size=k, replace=False)
        for j in range(k):
            popTurnir.append(pop[indexuriTurnir[j]])
        fitSTurnir = [indivTurnir[-1] for indivTurnir in popTurnir]
        valMaxTurnir = max(fitSTurnir)
        indexIndiv = fitSTurnir.index(valMaxTurnir)
        castigatorTurnir = pop[indexIndiv]
        pop2.append(castigatorTurnir)

    return pop2

pop2 = noua_generatie(pop1, 3)
print(pop2)