def Saludar():
    print("Hola mundo!")

def CalcularDoble(num):
    print(num*2)

def triplicar(num):
    print(num*3)

print("Llamar a la función Saludar")
Saludar()
input()

x = int(input("Ingrese un valor numérico para x: "))

print("Llamada a la función CalcularDoble (",x,")")
print("El doble de ",x," es ", end="") 
CalcularDoble(x)
print("El valor original de x es ",x)
input()

print("Llamada a la función Triplicar (",x,")")
triplicar(x)
print("El nuevo valor de x es ", x)