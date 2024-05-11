import numpy
'''
Functie de calculare a fitnessului
'''

def fitness(indiv):
    cost = 50 * indiv[0] + 70 * indiv[1] + 90 * indiv[2] + 60 * indiv[3] + 70 * indiv[4] + 100 * indiv[5]
    return 1 / cost

def generare_populatie_initiala(dim):
    pop = []
    for i in range(dim):
        valid = False
        while valid==False:
            Xbp = numpy.random.randint(0, 101)
            Xcp = 100 - Xbp

            Xbpe = numpy.random.randint(0, min(120 - Xbp, 60) + 1)
            Xcpe = 60 - Xbpe

            if Xcp + Xcpe <= 140:
                Xbc = numpy.random.randint(0, min(120 - Xbp - Xbpe, 80) + 1)
                Xcc = 80 - Xbc

                if Xcp + Xcpe + Xcc <= 140:
                    valid = True
                    indiv = [Xbp, Xbpe, Xbc, Xcp, Xcpe, Xcc]
                    fit = fitness(indiv)
                    indiv.append(fit)
                    pop.append(indiv)
    return pop

def check_indiv(indiv):
    if (indiv[0] + indiv[1] + indiv[2] > 120):
        return False
    if (indiv[3] + indiv[4] + indiv[5] > 140):
        return False
    if (indiv[0] + indiv[3] != 100):
        return False
    if (indiv[1] + indiv[4] != 60):
        return False
    if (indiv[2] + indiv[5] != 80):
        return False
    return True

'''
Selectia parintilor prin turnir
'''
def turnir(pop, k):
    pop_turnir = []
    for i in range(k):
        index = numpy.random.randint(0, len(pop))
        pop_turnir.append(pop[index])
    fitnesses = []
    for i in range(k):
        fitnesses.append(pop_turnir[i][-1])
    index_castigator = numpy.argmax(fitnesses)
    return pop_turnir[index_castigator]

def selectia_parintilor(pop, k):
    pop_parinti = []
    for i in range(len(pop)):
        indiv_castigator = turnir(pop, k)
        pop_parinti.append(indiv_castigator)
    return pop_parinti

'''
Generearea copiilor
'''
def recombinare_parinti(pop):
    pop_copii = pop.copy()
    for i in range(0, len(pop), 2):
        if i + 1 < len(pop):
            indiv1 = pop[i][:-1]
            indiv2 = pop[i+1][:-1]
            index = numpy.random.randint(0, len(pop[i]))
            copil1 = indiv1[:index] + indiv2[index:]
            copil2 = indiv2[:index] + indiv1[index:]
            copil1.append(fitness(copil1))
            copil2.append(fitness(copil2))
            pop_copii[i] = copil1.copy()
            pop_copii[i+1] = copil2.copy()
    return pop_copii

'''
Mutatie
'''
def mutatie(pop, prob_mut):
    pop_mutanti = []
    for indiv in pop:
        indiv_nou = indiv[:-1]
        for index in range(3):
            if numpy.random.uniform(0, 1) < prob_mut:
                val = numpy.random.randint(-1, 2)
                nou_val = indiv_nou[index] + val
                nou_val2 = indiv_nou[index + 3] - val
                if 0 <= nou_val <= 120 and 0 <= nou_val2 <= 140:
                    indiv_nou[index] = nou_val
                    indiv_nou[index + 3] = nou_val2
        indiv_nou.append(fitness(indiv_nou))
        pop_mutanti.append(indiv_nou)
    return pop_mutanti


'''
Functie de implementare a algoritmului
'''
def algoritm(dim, k):
    populatia_initiala = generare_populatie_initiala(dim)

    print("Populatie initiala: ")
    print(populatia_initiala)

    # print("\nVerificam daca toti indivizii sunt valizi")
    # for indiv in populatia_initiala:
    #     print(check_indiv(indiv))

    populatia_parinti = selectia_parintilor(populatia_initiala, k)
    populatia_copii = recombinare_parinti(populatia_parinti)
    populatia_copii_mutanti = mutatie(populatia_copii, 0.2)

    print("Populatie parintilor: ")
    print(populatia_parinti)

    print("Populatie copii: ")
    print(populatia_copii)

    print("Populatie mutatie: ")
    print(populatia_copii_mutanti)

'''
Apelarea algortimului
'''
algoritm(5, 3)