import numpy


def fitnessTSP(x, n, cost):
    fitness = 0
    for i in range(n - 1):
        fitness = fitness + cost[x[i]][x[i + 1]]
    fitness = fitness + cost[x[0]][x[n - 1]]
    return fitness


def gen(dim):
    cost = numpy.genfromtxt("costuri_tsp.txt")
    n = len(cost)
    pop = []
    for i in range(dim):
        x = numpy.random.permutation(n)
        fitness = fitnessTSP(x, n, cost)
        x = list(x)
        x = x + [fitness]
        pop = pop + [x]
    return numpy.asarray(pop)

# import TSP
# pop = TSP.gen(30)
