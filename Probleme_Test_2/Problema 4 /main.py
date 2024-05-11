import numpy
'''
Functie de calculare a fitnessului
'''

def fitness(indiv):
    cost = 50 * indiv[0] + 70 * indiv[1] + 90 * indiv[2] + 60 * indiv[3] + 70 * indiv[4] + 100 * indiv[5]
    return 1 / cost

# print("Fitness: [50, 60, 70, 80, 90, 100]: ", fitness([50, 60, 70, 80, 90, 100]))

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
print(generare_populatie_initiala(5))

def check_indiv(indiv):
    validation = True
    if (indiv[1] + indiv[2] + indiv[3] > 120):
        validation = False
    elif (indiv[3] + indiv[4] + indiv[5] > 140):
        validation = False
    elif (indiv[0] + indiv[3] != 100):
        validation = False