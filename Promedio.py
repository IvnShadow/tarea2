n = int(input("Ingrese cantidad de datos: "))

acum = 0

for i in range(n):
    print("Ingrese el dato", i+1, ": ")
    dato = float(input())
    acum = acum + dato

prom = float(acum/n)

print("El promedio es: ", prom)