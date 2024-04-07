#Problema TSP ( cu intoarcere din ultimul oras in primul )

#Avem matricea costurilor cu 0 pe diagonala principala
#Cum arata un individ x?
    # Un individ de numere intregi care arata ordinea in care au fost vizitate orasele
    # Dimensiune n -> numarul oraselor
    # Folosim permutarea pentru a respecta template ul individului
    # dim: de la 0 la n permutare
    # fitnessul ( calitatea ):
        # problema de minimizare
        # suma de la 0 la n-1 din cost( x[i] x[i+1] ) // separat de suma // + cost(x[0][-1], unde x este individul
# Nu avem restrictii pentru ca orice individ creat este fezabil

import numpy

def fitness_tsp(indiv, nr_gene, costS):
    fitness = 0
    for i in range(nr_gene - 1):
        fitness += costS(indiv[i], indiv[i+1])
    fitness += costS[indiv[0]][indiv[nr_gene-1]]   # costul de revenire de la locatia finala la cea initiala
    return fitness

def generare_populatie_initiala(dim):       # populatia are dim indivizi
    costS = numpy.genfromtxt("costuri_tsp.txt")

    populatie = []

    nr_gene = len(costS)
    for i in range(dim):    #creez dim indivizi
        indiv = numpy.random.permutation(nr_gene)
        fitness = fitness_tsp(indiv, nr_gene, costS)

        indiv = list(indiv)
        indiv.append(fitness)

        populatie.append(indiv)

    return populatie

# Pasul 3 - Selectia parintilor
    # Din populatia initiala creez o populatie de parinti prin selectie
    # Populatia de parinti va avea dim indivizi

# Pasul 4 - Populatia de parinti face copii ( Recombinarea parintilor )
    # Incrucisare / Cross Over intre parinti
    # Din fiecare pareche rezulta 2 copii
    # Pastram acelasi dim

# Pasul 5 - Mutatiile copiilor
    # se aplica din populatia de copii
    # dim constant

# Pasul 6 - Selectia generatiei urmatoare
    # se determina pe baza populatiei de copii mutanti si pe baza populatiei initiale

# Pana aici avem o generatie. Populatia redevine parinte de un numar dat de ori sau pana atingem valoarea ceruta