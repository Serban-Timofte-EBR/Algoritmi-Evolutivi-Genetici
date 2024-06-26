# Problema 11

# reprezentari binare din { 1, 2, .. 500 } -> individul este pe 9 biti

import numpy
from math import sin, cos

def binary_to_decimal(indiv):
    n = len(indiv)
    val = 0
    for i in range(n):
        val += (2 ** i) * indiv[n-i-1]
    return val

def fitness(indiv):
    val = binary_to_decimal(indiv)
    fitness = sin(val - 2) ** 2 - val * cos(2 * val)
    return val <= 500, fitness

def gen_pop(dim):
    pop = []
    for i in range(dim):
        flag = False
        while(flag == False):
            indiv = numpy.random.randint(0 , 2, size = 9)
            flag, fit = fitness(indiv)
        indiv = list(indiv)
        indiv.append(fit)
        pop.append(indiv)
    return pop

populatie_initiala = gen_pop(10)
print(numpy.asarray(populatie_initiala))

# def turneu(pop, k, dim):
#     pop_parinti = []
#     for i in range(dim):
#         indexuri_indivizi_turnir = numpy.random.randint(0, dim, k)
#         lista_fit = []
#         for j in range(k):
#             fit = pop[indexuri_indivizi_turnir[j]][-1]
#             lista_fit.append(fit)
#         index_val_max = numpy.argmax(lista_fit)

# Problema 7

def fitness(indiv):    # de tip permutare
    counter = 0
    n = len(indiv)
    for i in range(n - 1):
        for j in range(i+1, n):
            if indiv[i] == indiv[j] and indiv[j] == indiv[i]:
                counter += 1
    return counter

def pop_permutari(dim, nr_gene):
    pop = []
    for i in range(dim):
        indiv = numpy.random.permutation(nr_gene)
        fit = fitness(indiv)
        indiv = list(indiv)
        indiv.append(fit)
        pop.append(indiv)
    return pop

pop_i_permutari = pop_permutari(20, 20)
print(numpy.asarray(pop_i_permutari))