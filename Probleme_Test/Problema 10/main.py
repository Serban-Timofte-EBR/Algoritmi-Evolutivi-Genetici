import numpy

def dec_to_gray(decVal):
    gray_x = bin(decVal ^ (decVal >> 1))[2:].zfill(9)
    gray_ints = [int(bit) for bit in gray_x]
    return gray_ints

print(dec_to_gray(10))

def fitness(indivDec):
    return indivDec ** 2

def generare_populatie(dim):
    population = []
    for i in range(dim):
        indiv = []
        val = numpy.random.randint(0, 351)
        grayVal = dec_to_gray(val)
        for i in range(9):
            indiv.append(grayVal[i])
        indiv.append(fitness(val))
        population.append(indiv)
    return population

pop1 = generare_populatie(5)
print(pop1)

def turnir(pop1, k):
    pop2 = []
    dim = len(pop1)
    for i in range(len(pop1)):
        turnirPop = []
        indexesTurnir = numpy.random.choice(len(pop1), size = k, replace=False)
        for i in range(len(indexesTurnir)):
            turnirPop.append(pop1[indexesTurnir[i]])
        fitnessuriTurnir = [indiv[-1] for indiv in turnirPop]
        fitMax = max(fitnessuriTurnir)
        indexFitmax = fitnessuriTurnir.index(fitMax)
        pop2.append(turnirPop[indexFitmax])
    return pop2

print("Populatia 2:")
pop2 = turnir(pop1, 2)
print(pop2)