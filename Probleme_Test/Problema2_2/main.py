import math
import numpy


def dec_to_binary(val):
    bin_str = bin(val)[2:].zfill(12)
    bin_rep = [int(bit) for bit in bin_str]
    return bin_rep

# Preluam 12 biti si intoarcem valaorea
def binary_to_dec(binary_list):
    decVal = 0
    for i in range(12):
        decVal += binary_list[i] * 2**(12-i-1)
    return decVal

# Individul este reprezentat pe 24 de biti (12 pentru x si 12 pentru y)
def fitness(indiv):
    x_bin = indiv[:12]
    y_bin = indiv[12:]
    x = binary_to_dec(x_bin)
    y = binary_to_dec(y_bin)
    return (y-1) * (math.sin(x-2)) ** 2

def generare_populatie(dim):
    pop = []
    for i in range(dim):
        indiv = []
        xDec = numpy.random.randint(1, 1501)
        yDec = numpy.random.randint(0, 2502)
        x_bin = dec_to_binary(xDec)
        y_bin = dec_to_binary(yDec)
        for i in range(12):
            indiv.append(x_bin[i])
        for i in range(12):
            indiv.append(y_bin[i])
        indiv.append(fitness(indiv))
        pop.append(indiv)
    return pop

pop = generare_populatie(5)
print(pop)

def mutatie_multipunct(pop, pc):
    popc = pop.copy()
    for i in range(0, len(pop), 2):
        if numpy.random.uniform(0,1) < pc and i+1 < len(pop):
            indexes = list(numpy.random.choice(range(len(popc)), size=3, replace=False))
            index1 = min(indexes)
            index3 = max(indexes)
            indexes.remove(index1)
            indexes.remove(index3)
            index2 = indexes[0]

            indiv1 = pop[i]
            indiv2 = pop[i+1]

            copil1 = indiv1[:index1] + indiv2[index1:index2] + indiv1[index2:index3] + indiv2[index3:-1]
            copil2 = indiv2[:index1] + indiv1[index1:index2] + indiv2[index2:index3] + indiv1[index3:-1]

            popc[i] = copil1.copy()
            popc[i+1] = copil2.copy()

            popc[i][-1] = fitness(copil1)
            popc[i+1][-1] = fitness(copil2)
    return popc

popc = mutatie_multipunct(pop, 0.5)
print(popc)