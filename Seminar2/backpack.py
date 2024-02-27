print("Welcome to the PEAG Sem 02 - 27.02")
print("Problema Rucsacului | Backpack Problem\n")

import numpy

# verificam daca individul este fezabil sau nu + return vezabilitate
# calculam costul total al individului
# calculam valoarea individului
def individul_checker(gene_individ, nr_gene, costS, valS, costMax):
    # in x sunt genele
    # in v este valoarea fiecarei gene
    fitness = 0
    cost = 0

    for i in range(nr_gene):
        fitness += gene_individ[i] * valS[i]
        cost += gene_individ[i] * costS[i]

    return cost <= costMax, fitness # intoarce daca individul este fezabil si fitness-ul ( calitatea )

def generare_indivizi(costMax, dim):
    costS = numpy.genfromtxt("costs.txt")
    valS = numpy.genfromtxt("vals.txt")
    n = len(costS)

    populatie = []

    for i in range(dim):
        flag = False
        while flag == False:
            #indiv = numpy.random.randint(0, 2, n)   # valori int de la 0 la 1 in numar de n (adica cate costuri/valori )
            # pentru continuu folosim:
            indiv = numpy.random.uniform(0, 1, n)
            flag, fitness = individul_checker(indiv, n, costS, valS, costMax)
        #aici vom avea un individ fezabil

        #adaugam fitnessul la finalul genelor
        indiv = list(indiv)
        indiv.append(fitness)# fitness este vazut ca element pe care il adauga in lista
        populatie.append(indiv)

    return numpy.asarray(populatie)     # mai bun pentru vizualizare - return populatie

pop = generare_indivizi(30, 10)
print(pop)

# sau py console:
# import backpack
# pop = backpack.generare_indivizi(30,10)

