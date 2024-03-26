import numpy

######################## CALCUL FUNCTIE FITNESS + FEZ ######################
def ok(x, n, c, v, cmax):
    fitness = 0
    cost = 0
    for i in range(n):
        fitness = fitness + x[i] * v[i]
        cost = cost + x[i] * c[i]
    return cost <= cmax, fitness

########################## GENERAREA UNEI POPULATII ########################
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


######################### OPERATOR MUTATIE NEUNIFORMA #######################
def m_neuniforma(gena, sigma, a, b):
    zgomot = numpy.random.normal(0, sigma)
    gena_mutanta = gena + zgomot
    if gena_mutanta > b:
        gena_mutanta = b
    if gena_mutanta < a:
        gena_mutanta = a
    return gena_mutanta


########################## OPERATOR MUTATIE UNIFORMA ########################

def m_uniforma(a, b):
    gena_mutanta = numpy.random.uniform(a, b)
    return gena_mutanta


########################## APLICARE MUTATIE POPULATIE #########################
def mutatie_populatie(pop, dim, n, c, v, cost_max, probabilitate_m, sigma):
    pop_m = pop.copy()
    for i in range(dim):
        x = pop[i][:n].copy()
        for j in range(n):
            r = numpy.random.uniform(0, 1)
            if r <= probabilitate_m:
                x[j] = m_neuniforma(x[j], sigma, 0, 1)
                #SAU x[j] = m_uniforma(0, 1)
        fez, val = ok(x, n, c, v, cost_max)
        if fez:
            x = x + [val]
            pop_m[i] = x.copy()
    return pop_m



'''
import RucsacContinuu
populatie,dim,n,c,v,cost_max = RucsacContinuu.gen(30, 10)
populatie_m = RucsacContinuu.mutatie_populatie(populatie, dim, n, c, v, cost_max, 0.1, 0.15)
import numpy
populatie = numpy.asarray(populatie)
populatie_m = numpy.asarray(populatie_m)
'''

def crossover_singular(indiv1, indiv2, n, alpha):
    index = numpy.random.randint(0, n)
    copil1 = indiv1.copy()
    copil2 = indiv2.copy()
    copil1[index] = indiv1[index] * alpha + indiv2[index] * (1-alpha)
    copil2[index] =indiv2[index] * alpha + indiv1[index] * (1-alpha)
    return copil1, copil2

def crossover_simplu(indiv1, indiv2, n, alpha):
    index = numpy.random.randint(0, n)
    copil1 = indiv1.copy()
    copil2 = indiv2.copy()
    for i in range(index, n):
        copil1[i] = indiv1[i] * alpha + indiv2[i] * (1 - alpha)
        copil2[i] = indiv2[i] * alpha + indiv1[i] * (1 - alpha)
    return copil1, copil2

def crossover_total(indiv1, indiv2, n, alpha):
    copil1 = indiv1.copy()
    copil2 = indiv2.copy()
    for i in range(n):
        copil1[i] = indiv1[i] * alpha + indiv2[i] * (1 - alpha)
        copil2[i] = indiv2[i] * alpha + indiv1[i] * (1 - alpha)
    return copil1, copil2

def crossover_populatie(pop, dim, n, c, v, cmax, probabilitate_crossover, alpha):
    copii = pop.copy()
    for i in range(0, dim, 2):
        indiv1 = copii[i][0:n].copy()
        indiv2 = copii[i + 1][0:n].copy()
        r = numpy.random.uniform(0,1)
        if(r<probabilitate_crossover):
            copil1, copil2 = crossover_simplu(indiv1, indiv2, n, alpha)
            flag, fitness = ok(copil1, n, c, v, cmax)
            if(flag):
                copil1 = copil1 + [fitness]
                copii[i] = copil1.copy()
            #else - copiez parintele, dar este deja
            flag, fitness = ok(copil2, n, c, v, cmax)
            if(flag):
                copil2 = copil2 +[fitness]
                copii[i+1] = copil2.copy()
    return copii

'''
import RucsacContinuu
populatie,dim,n,c,v,cost_max = RucsacContinuu.gen(30, 10)
copii = RucsacContinuu.crossover_populatie(populatie, dim, n, c, v, cost_max, 0.70, 0.20)
import numpy
populatie = numpy.asarray(populatie)
copii = numpy.asarray(copii)
'''

"""
Selectia:
    1. Turnir
        - de dim ori selectez k indivizi
        - cel mai bun define parinte
    2. Ruleta
        - Determinam FPS
            - vector cu toate valorile fitness din populatie
            - se face suma vectorului
            - fps se face impartind fiecare element din vector la suma totala
            - q fps se face:
                - prima valoarea se copiaza 
                - de la a doua valaorea se face suma celor de dinainte plus elementul curent 
            - se reprezinta valorile. Se alege o valaorea aleatoare fiecarui interval. In functie de intervalul din care
            este extrasa valoarea, se alege parintele
            - se aleg dim valori aleatoare
    3. SUS
        - se repeta ruleta, dar selectia se face diferit
        - plecam de la o valaore r din [0, 1/dim] si aleg parintele in fucntie de valoarea
        - adaug la r 1/dim
"""

def fps(fitnessuri, dim):
    fps = numpy.zeros(dim)
    suma = numpy.sum(fitnessuri)
    for i in range(dim):
        fps[i] = fitnessuri[i]/suma
    qfps = fps.copy()
    for i in range(1, dim):
        qfps[i] = qfps[i-1] + fps[i]
    return qfps

def ruleta(pop_initiala, dim, n):   # n = numar gene dintr-un individ
    pop_initiala = numpy.array(pop_initiala)
    parinti = pop_initiala.copy()
    fitnessuri = numpy.zeros(dim, dtype=float)
    for i in range(dim):
        fitnessuri[i] = pop_initiala[i][-1]
    qfps = fps(fitnessuri, dim)
    for i in range(dim):
        r = numpy.random.uniform(0,1)
        pozitie = numpy.where(qfps >= r)
        indexBuzunarRuleta = pozitie[0][0]
        #copiem gene
        parinti[i][0:n] = pop_initiala[indexBuzunarRuleta][0:n]
        #copiem fitnessul
        parinti[i][n] = fitnessuri[indexBuzunarRuleta]
    return parinti

def selectieparinti():
    pop_initiala, dim, n, c, v, cost_max = gen(30, 10)
    parinti = ruleta(pop_initiala, dim, n)
    return pop_initiala, parinti