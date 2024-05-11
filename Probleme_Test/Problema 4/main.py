'''
Functie de calculare a fitnessului
'''

def fitness(indiv):
    cost = 50 * indiv[0] + 70 * indiv[1] + 90 * indiv[2] + 60 * indiv[3] + 70 * indiv[4] + 100 * indiv[5]
    return 1 / cost

print("Fitness: [50, 60, 70, 80, 90, 100]: ", fitness([50, 60, 70, 80, 90, 100]))