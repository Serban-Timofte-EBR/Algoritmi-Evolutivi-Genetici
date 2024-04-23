"""
    Determinati o aranjare circulara pentru n caini si m pisici a.i. intre oricare 2 caini consecutivi
sa nu se afle o pisica sau sa se afle minim 2
n = 5
m = 3
"""

'''
    Varianta 1: Binar 
    0 - caine
    1 - pisica
    
    !!! Determinati, gasiti, etc - avem indivizi valizi, fezabili ( este valid daca are 8 gene ) => fara restrictii
    !!! O pisica intre doi caini este fezabil 
    
    !!! Vreau sa evit Caine - Pisica - Caine ( 0 - 1 - 0 )
    FITNESS: 
        - 1 / (numarul de perechi 0 - 1 - 0) din individ
    
    GENERAREA POPULATIEI URMATOARE:
        - Consideram un vector initial x = [0, 0, 0, 0, 0, 1, 1, 1]
        - Shuffle dupa
'''

import numpy

def fitness(indiv, nr_caini, nr_pisici):
    contor = 0
    for i in range(nr_caini + nr_pisici - 2):
        if indiv[i] == 0  and indiv[i+1] == 1 and indiv[i+2] == 0:
            contor += 1
    #Handle edge cases
    # prima gena cu ultimele 2
    if indiv[-1] == 0 and indiv[0] == 1 and indiv[1] == 0:
        contor += 1
    #ultima gena cu primele 2
    elif indiv[-1] == 0 and indiv[0] == 1 and indiv[1] == 1:
        contor += 1
    return 1 / (1 + contor) # transformam in problema de minimizare

def pop_init(dim, nr_caini, nr_pisici):
    pop = []
    for i in range(dim):
        indiv = numpy.zeros(nr_caini + nr_pisici)
        indiv[0:nr_caini] = numpy.zeros(nr_caini)
        indiv[nr_caini:] = numpy.ones(nr_pisici)
        numpy.random.shuffle(indiv)
        fit  = fitness(indiv, nr_caini, nr_pisici)
        indiv = list(indiv)
        indiv.append(fit)
        pop.append(indiv)
    return pop

if __name__ == '__main__':
    pop = pop_init(10, 5, 3)
    print(numpy.asarray(pop))


'''
    Varianta 2 - permutari
    0 1 2 3 4 - caini
'''