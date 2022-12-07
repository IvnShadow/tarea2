def menu():
    print("Menú de recomendaciones")
    print("   1. Literatura")
    print("   2. Cine")
    print("   3. Música")
    print("   4. Videojuegos")
    print("   5. Salir")

def menliteratura():
    print("Lecturas recomendables:")
    print(" + Esperándolo a Tito y otros cuentos de fúbol (Eduardo Sacheri)")
    print(" + El juego de Ender (Orson Scott Card)")
    print(" + El sueño de los héroes (Adolfo Bioy Casares)")

def mencine():
    print("Películas recomendables:")
    print(" + Matrix (1999)")
    print(" + El último samuray (2003)")
    print(" + Cars (2006)")

def menmusica():
    print("Discos recomendables:")
    print(" + Despedazado por mil partes (La Renga, 1996)")
    print(" + Búfalo (La Mississippi, 2008)")
    print(" + Gaia (Mägo de Oz, 2003)")

def menjuegos():
    print("Videojuegos clásicos recomendables")
    print(" + Día del tentáculo (LucasArts, 1993)")
    print(" + Terminal Velocity (Terminal Reality/3D Realms, 1995)")
    print(" + Death Rally (Remedy/Apogee, 1996)")

def mensalir():
    print("Gracias, vuelva pronto")
    
opc=0

while opc != 5:
   
    menu()

    opc = int(input("Ingrese opción: "))

    if opc == 1:
        menliteratura()
        input("Presione enter para continuar")
    elif opc == 2:
        mencine()
        input("Presione enter para continuar")
    elif opc == 3:
        menmusica()
        input("Presione enter para continuar")
    elif opc== 4:
        menjuegos()
        input("Presione enter para continuar")
    elif opc == 5:
        mensalir()
    else:
        print("Opción no válida")
        input("Presione enter para continuar")


