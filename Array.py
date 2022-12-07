A = []
tamaño = 10

import random

for i in range(tamaño):
    A.append(random.randint(0,100))

print("Los elementos del arreglo son: ")
print (A)

print("En orden inverso: ")
A.reverse()
print(A)