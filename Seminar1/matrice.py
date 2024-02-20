import numpy

#creare matricde de 4x5

mat = numpy.zeros([4,5], dtype = "double")
print(mat)

#pe matricea 4x4 copiem valorile din fisier

mat[0:4, 0:4] = numpy.genfromtxt("date.txt")    # 0:4 inseamna 0,1,2,3 ( si linii si coloane )

print("Matricea dupa citire din fisier")
print(mat)

for i in range(4):
    mat[i, -1] = numpy.sum(mat[i, 0:4])

print("Matricea dupa modificarea ultimei coloana")
print(mat)

# Generare matrice 5x3 cu valori aleatoare
    # Distributia normala = Clopotul lui Gauss = Valorile din mijlocul intervalului au sanse mai mari de a selectate
    # Distributia uniforma = Sanse egale de selectare

mat_aleatoare = numpy.random.uniform(-1, 1, [5,3])
print(mat_aleatoare)

#Generati o matrice 20x5 cu val aleatoare din distributia normala si calculati lista
#de dimensiune 1x20 cu media valorilor pt fiecare linie din matricea initiala
