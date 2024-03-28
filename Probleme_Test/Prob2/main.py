# functia f(x,y) = y * (sin(x-2))**2
# [x, y] din {1,2, ..., 1500} x {-1, 0, ..., 2500}
# genotip şir binar obţinut prin reprezentarea în bază 2 a fiecărei componente a fenotipului
import math
import random

import numpy

def fitness(x, y):
    return y * (math.sin(x-2))**2

def transformare_binar(lista):
    binar = lista.copy()
    for i in range(0, len(lista)):
        binar[i] = format(lista[i], "b")
    return binar

def generare_populatie(dim):
    populatie = []
    for i in range(dim):
        x = random.randint(1, 1501)
        y = random.randint(-1, 2501)
        fit = fitness(x,y)
        gene = []
        gene.append(x)
        gene.append(y)
        indiv = transformare_binar(gene)
        indiv = indiv + [fit]
        populatie = populatie + [indiv]
    return populatie

def recombinare_multipunct(parinte1, parinte2, pc):
    x1, y1 = parinte1[0], parinte1[1]
    x2, y2 = parinte2[0], parinte2[1]

    copil1_x, copil1_y = "", ""
    copil2_x, copil2_y = "", ""

    r = numpy.random.uniform(0,1)
    if r < pc:
        len_min_x = min(len(x1), len(x2))
        len_min_y = min(len(y1), len(y2))

        puncte_x = sorted(numpy.random.choice(range(1, len_min_x), 3, replace=False))
        puncte_y = sorted(numpy.random.choice(range(1, len_min_y), 3, replace= False))

        copil1_x = x1[0:puncte_x[0]] + x2[puncte_x[0]: puncte_x[1]] + x1[puncte_x[1]:puncte_x[2]] + x2[puncte_x[2]:]
        copil2_x = x2[0:puncte_x[0]] + x1[puncte_x[0]: puncte_x[1]] + x2[puncte_x[1]:puncte_x[2]] + x1[puncte_x[2]:]

        copil1_y = y1[0:puncte_y[0]] + y2[puncte_y[0]:puncte_y[1]] + y1[puncte_y[1]:puncte_y[2]] + y2[puncte_y[2]:]
        copil2_y = y2[0:puncte_y[0]] + y1[puncte_y[0]:puncte_y[1]] + y2[puncte_y[1]:puncte_y[2]] + y1[puncte_y[2]:]

        if int(copil1_x, 2) > 1500 or int(copil1_y, 2) > 2500:
            copil1_x = x1
            copil1_y = y1

        if int(copil2_x, 2) > 1500 or int(copil2_y, 2) > 2500:
            copil2_x = x2
            copil2_y = y2

    else:
        copil1_x, copil2_x = x1, x2
        copil1_y, copil2_y = y1, y2

    dec_copil1_x = int(copil1_x, 2)
    dec_copil1_y = int(copil1_y, 2)
    dec_copil2_x = int(copil2_x, 2)
    dec_copil2_y = int(copil2_y, 2)
    fitness_copil1 = fitness(dec_copil1_x, dec_copil1_y)
    fitness_copil2 = fitness(dec_copil2_x, dec_copil2_y)

    return [copil1_x, copil1_y, fitness_copil1], [copil2_x, copil2_y, fitness_copil2]


def generare_noua_populatie(populatie, dim, pc):
    noua_populatie = populatie.copy()
    for i in range(0, dim, 2):
        indiv1 = populatie[i].copy()
        if i+1 < dim:
            indiv2 = populatie[i+1].copy()
            copil1, copil2 = recombinare_multipunct(indiv1, indiv2, pc)
            noua_populatie[i] = copil1.copy()
            noua_populatie[i+1] = copil2.copy()
        else:
            noua_populatie[i] = indiv1.copy()
    return noua_populatie

pop = generare_populatie(12)
print("Populatie initiala ")
print(pop)
generatie_copii = generare_noua_populatie(pop, 5, 0.5)
print("Populatie copii ")
print(generatie_copii)