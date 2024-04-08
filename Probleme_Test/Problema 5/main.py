import numpy

#Transmitem individul ca sir de biti
def bin_to_dec(indiv):
    val = 0
    for i in range(len(indiv)):
        val += indiv[i] * (2**(len(indiv) - i - 1))
    return val

def fitness(indiv):
    fit = 0
    for i in range(len(indiv) - 1):
        fit += indiv[i]
    return fit

def generare_populatie(dim):
    pop = []
    for i in range(dim):
        indiv = []
        for _ in range(7):
            gena = numpy.random.randint(0,2)
            indiv.append(gena)
            fit = fitness(indiv)
        indiv.append(fit)
        pop.append(indiv)
    return pop

pop = generare_populatie(5)
print(pop)

def recombinare_multipunct(pop, pc):
    popc = pop.copy()
    n = len(pop[0])
    for i in range(0, len(popc), 2):
        indiv_1 = pop[i]
        if i+1 < len(popc):
            indiv_2 = pop[i+1]
            index1 = numpy.random.randint(0, len(pop))
            index2 = index1
            while index2 == index1:
                index2 = numpy.random.randint(0, len(pop))
            if index2 < index1:
                temp = index2
                index2 = index1
                index1 = temp
            if numpy.random.uniform(0, 1) < pc:
                copil1 = indiv_1[:index1] + indiv_2[index1:index2] + indiv_1[index2:]
                copil2 = indiv_2[:index1] + indiv_1[index1:index2] + indiv_2[index2:]
                popc[i][0:n] = copil1.copy()
                popc[i+1][0:n] = copil2.copy()
                popc[i][-1] = fitness(copil1)
                popc[i+1][-1] = fitness(copil2)
    return popc

popc = recombinare_multipunct(pop, 0.2)
print(popc)