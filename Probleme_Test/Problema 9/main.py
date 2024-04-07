# Trimis ca sir de biti fara fitness
import math

import numpy.random

def bin_to_dec(indiv):
    val = 0
    for i in range(len(indiv)):
        val += indiv[i] * (2**(len(indiv) - i - 1))
    return val

def checker(indiv):
    decVal = bin_to_dec(indiv)
    return decVal <= 2500

# Trimis ca numarul in dec
def fitness(indiv):
    decVal = bin_to_dec(indiv)
    return math.sin(decVal - 2)**2

def gen_pop(dim):
    population = []
    for i in range(dim):
        # reprezentarea se face pe 12 biti
        valid_indiv = False
        while(valid_indiv == False):
            indiv = []
            for j in range(12):
                x = numpy.random.randint(0, 2)
                indiv.append(x)
            valid_indiv = checker(indiv)
        fit = fitness(indiv)
        indiv.append(fit)
        population.append(indiv)
    return population

populatie_initiala = gen_pop(5)
print(populatie_initiala)

def sigma_scalare(fitnessuri):
    medie = numpy.mean(fitnessuri)
    std_fit = numpy.std(fitnessuri)
    if std_fit == 0:
        return fitnessuri
    fitnessuri_scalate = fitnessuri.copy()
    for i in range(len(fitnessuri)):
        fitnessuri_scalate[i] = fitnessuri[i] - (medie - 2 * std_fit)
        if fitnessuri_scalate[i] < 0:
            fitnessuri_scalate[i] = 0
    return fitnessuri_scalate

def fps(fitnessuri):
    sumFit = sum(fitnessuri)
    fps = [fitnessuri[i] / sumFit for i in range(len(fitnessuri))]
    qfps = fitnessuri.copy()
    for i in range(1, len(fitnessuri)):
        qfps[i] = fps[i] + qfps[i-1]
    return qfps

def ruleta(pop_init):
    pop_parinti = pop_init.copy()
    n = len(pop_init[0])
    fitnessuri = [indiv[-1] for indiv in pop_init]
    # sigma-scalare
    fitnessuri_scalate = sigma_scalare(fitnessuri)
    qfps = fps(fitnessuri_scalate)
    for i in range(len(pop_init)):
        r = numpy.random.uniform(0, 1)
        qfps = numpy.array(qfps)
        poz = numpy.where(qfps >= r)[0][0]
        pop_parinti[i][0:n] = pop_init[poz][0:n]
        pop_parinti[i][-1] = fitnessuri[poz]
    return pop_parinti

pop2 = ruleta(populatie_initiala)
print(pop2)