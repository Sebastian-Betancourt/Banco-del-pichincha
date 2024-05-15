#ENTRADA DE DATOS
import time
def tiempo():
    print ("Procesando los datos")
    print ("Porfavor espere")
    time.sleep(3)
nombre = input ("Ingrese su nombre porfavor: ")
tipoTargeta = int (input ("Ingrese su tipo de targeta: "))
creditoA = float (input("Ingrese el credito anterior: "))
match (tipoTargeta):
    case 1:
        tiempo()
        procentage= creditoA * 0.25
        creditoActual= procentage + creditoA
        print(f"El credito ha aumentado un 25% dando un total de: {creditoActual}")
    case 2:
        tiempo()
        procentage= creditoA * 0.35
        creditoActual= procentage + creditoA
        print(f"El credito ha aumentado un 35% dando un total de: {creditoActual}")
    case 3:
        tiempo()
        procentage= creditoA * 0.40
        creditoActual= procentage + creditoA
        print(f"El credito ha aumentado un 40% dando un total de: {creditoActual}")
    case _:
        tiempo()
        procentage= creditoA * 0.50
        creditoActual= procentage + creditoA
        print(f"El credito ha aumentado un 50% dando un total de: {creditoActual}")#ENTRADA DE DATOS
import time
def tiempo():
    print ("Procesando los datos")
    print ("Porfavor espere")
    time.sleep(3)
nombre = input ("Ingrese su nombre porfavor: ")
tipoTargeta = int (input ("Ingrese su tipo de targeta: "))
creditoA = float (input("Ingrese el credito anterior: "))
match (tipoTargeta):
    case 1:
        tiempo()
        procentage= creditoA * 0.25
        creditoActual= procentage + creditoA
        print(f"El credito ha aumentado un 25% dando un total de: {creditoActual}")
    case 2:
        tiempo()
        procentage= creditoA * 0.35
        creditoActual= procentage + creditoA
        print(f"El credito ha aumentado un 35% dando un total de: {creditoActual}")
    case 3:
        tiempo()
        procentage= creditoA * 0.40
        creditoActual= procentage + creditoA
        print(f"El credito ha aumentado un 40% dando un total de: {creditoActual}")
    case _:
        tiempo()
        procentage= creditoA * 0.50
        creditoActual= procentage + creditoA
        print(f"El credito ha aumentado un 50% dando un total de: {creditoActual}")