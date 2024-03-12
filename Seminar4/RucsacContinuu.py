import numpy

def ok(x, n, c, v, cmax):
    fitness = 0
    cost = 0
    for i in range(n):
        fitness = fitness + x[i] * v[i]
        cost = cost + x[i] * c[i]
    return cost <= cmax, fitness


def gen(cmax, dim):
    c = numpy.genfromtxt("cost.txt")
    v = numpy.genfromtxt("valoare.txt")
    n = len(c)
    pop = []
    for i in range(dim):
        flag = False
        while flag == False:
            x = numpy.random.uniform(0, 1, n)
            flag, fitness = ok(x, n, c, v, cmax)
        x = list(x)
        x = x + [fitness]
        pop = pop + [x]
    return pop, dim, n, c, v, cmax

# Apel
# import RucsacContinuu
# pop = RucsacContinuu.gen(30, 10)

# se adauga o valoare de zgomot ( o valaore foarte mica pentru a nu schimba individul => gena mutanta
# zgomot <= distributia normala
def m_neuniforma(gena, sigma, a, b):    # a,b inteval de definire a genelor
    zgomot = numpy.random.normal(0, sigma)
    gena_mutanta = gena + zgomot
    if(gena_mutanta > b):
        gena_mutanta  = b
    elif(gena_mutanta < a ):
        gena_mutanta = a
    return gena_mutanta

def mutatie_populatie(pop, dim, n, c, v, cmax, probabilitate_mutatie, sigma):
    pop_muntanta = pop.copy()   #deep-copy
    for i in range(dim):
        individ = pop[i][0:n].copy   #excludem ultima coloana cu fitness-ul => extragem genele
        for j in range(n):  #n = numarul de gene
            r = numpy.random.uniform(0, 1)
            if(r < probabilitate_mutatie):
                individ[j] = m_neuniforma(individ[j], sigma, 0, 1)
        cost, fitness = ok(individ, n, c, v, cmax)
        if(cost):
            indiv = indiv + [fitness]
            pop_muntanta[i] = indiv.copy()
    return pop_muntanta

#How to run the code? Follow these instructions:
'''
import RucsacContinuu
pop, dim, n , c, v, cmax = RucsacContinuu.mutatie_populatie(pop, dim, n, c, v, cmax, 0.2, 0.25)
import numpy
pop = numpy.asarray(pop)
pop_m = numpy.asarray(pop_m)
'''