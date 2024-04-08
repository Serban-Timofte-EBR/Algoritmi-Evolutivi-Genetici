import numpy

def fitness(indiv):
    nr_gene = len(indiv)
    fit = 0
    for i in range(nr_gene - 1):
        for j in range(i + 1, nr_gene):
            if indiv[i] == j and indiv[j] == i:
                fit += 1
    return fit

def generare_populatie_initiala(dim, nr_gene):
    pop = []
    for i in range(dim):
        indiv = numpy.random.permutation(nr_gene)
        indiv = list(indiv)
        indiv.append(fitness(indiv))
        pop.append(indiv)
    return pop

pop = generare_populatie_initiala(5, 5)
print(pop)

def mutatie_inserare(pop, pm):
    dim = len(pop)
    for i in range(dim):
        if numpy.random.uniform() < pm:
            n = len(pop[i]) - 1
            index1, index2 = numpy.random.choice(range(n), size=2, replace=False)
            valoare_de_inserat = pop[i].pop(index2)
            pop[i].insert(index1 + 1, valoare_de_inserat)
    return pop

pop2 = mutatie_inserare(pop, 0.8)
print(pop2)