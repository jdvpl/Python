from math import pi

def area_rectangulo(base,altura):
    return(base*altura)

def area_circulo(radio):
    return(pi * radio**2)

def area_total(arg1, arg2, arg3, arg4):
    return(arg1 + arg2 + arg3 + arg4)

def calculo():
    base1 = float(input("Ingrese la base del rectángulo 1: "))
    altura1 = float(input("Ingrese la altura del rectángulo 1: "))

    base2 = float(input("Ingrese la base del rectángulo 2:"))
    altura2 = float(input("Ingrese la altura del rectángulo 2: "))

    radio1 = float(input("Ingrese el radio del círculo 1:"))
    radio2 = float(input("Ingrese el radio del círculo 2:"))

    area = area_total(area_rectangulo(base1,altura1), area_rectangulo(base2,altura2), area_circulo(radio1), area_circulo(radio2))

    #a_rectangulo1 = area_rectangulo(base1,altura1)
    #a_rectangulo2 = area_rectangulo(base2,altura2)
    #a_circulo1 = area_circulo(radio1)
    #a_circulo2 = area_circulo(radio2)

    #area = area_total(a_rectangulo1, a_rectangulo2, a_circulo1, a_circulo2)
    print("suma total =", area)

calculo()