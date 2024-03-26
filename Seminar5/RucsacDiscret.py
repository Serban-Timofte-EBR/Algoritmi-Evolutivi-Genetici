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
            x = numpy.random.randint(0, 2, n)
            flag, fitness = ok(x, n, c, v, cmax)
        x = list(x)
        x = x + [fitness]
        pop = pop + [x]
    return pop, dim, n, c, v, cmax


########################### OPERATOR MUTATIE BINARA #########################
def m_binara(gena):
    gena_mutanta = not gena
    return int(gena_mutanta)  # cast pentru trecerea True/False in 1/0


########################## APLICARE MUTATIE POPULATIE #########################
def mutatie_populatie(pop, dim, n, c, v, cost_max, probabilitate_m):
    pop_m = pop.copy()
    for i in range(dim):
        x = pop[i][:n].copy()
        for j in range(n):
            r = numpy.random.uniform(0, 1)
            if r <= probabilitate_m:
                x[j] = m_binara(x[j])
        fez, val = ok(x, n, c, v, cost_max)
        if fez:
            x = x + [val]
            pop_m[i] = x.copy()
    return pop_m


'''
import RucsacDiscret
populatie,dim,n,c,v,cost_max = RucsacDiscret.gen(30, 10)
populatie_m = RucsacDiscret.mutatie_populatie(populatie, dim, n, c, v, cost_max, 0.1)
import numpy
populatie = numpy.asarray(populatie)
populatie_m = numpy.asarray(populatie_m)
'''

def crossover_unipunct(indiv1, indiv2, n):
    index = numpy.random.randint(0, n)
    copil1 = indiv1.copy()
    copil2 = indiv2.copy()

    copil1[0:index] = indiv1[0:index]   # redundant
    copil1[index:n] = indiv2[index:n]

    copil2[0:index] = indiv2[0:index]   # redundant
    copil1[index:n] = indiv2[index:n]

    return copil1, copil2

def crossover_populatie(pop, dim, n, c, v, cmax, probabilitate_crossover):
    copii = pop.copy()
    for i in range(0, dim, 2):
        indiv1 = copii[i][0:n].copy()
        indiv2 = copii[i + 1][0:n].copy()
        r = numpy.random.uniform(0,1)
        if(r<probabilitate_crossover):
            copil1, copil2 = crossover_unipunct(indiv1, indiv2, n)
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
import RucsacDiscret 
populatie,dim,n,c,v,cost_max = RucsacDiscret.gen(30, 10)
copii = RucsacDiscret.crossover_populatie(populatie, dim, n, c, v, cost_max, 0.70)
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