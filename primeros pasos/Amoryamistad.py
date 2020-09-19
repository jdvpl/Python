import os
#amor y amistad
print("#############################################".center(50))
print("Quieres saber si estas enamorado?".center(50))
print("#############################################".center(50))
Nombre=input("Escribe tu nombre ")
while True:
    try:
        Edad = int(input("Escribe tu edad "))
        break
    except ValueError:
        print("El valor es incorrecto, debes ingresar un numero entero")

Soledad=input("Sientes algo por alguien? \nS (Si) \nN (no)\n")
while not((Soledad=="N")or(Soledad=="S")or(Soledad=="n")or(Soledad=="s")):
    print("Opcion Incorrecta")
    Soledad=input("Vives solo? \nS (Si) \nN (no)\n")
novia=input("Tienes novia(o)? \nS (Si) \nN (no)\n")
while not((novia=="N")or(novia=="S")or(Soledad=="n")or(Soledad=="s")):
    print("Opcion Incorrecta")
    novia=input("Tienes novia(o)? \nS (Si) \nN (no)\n")
if((novia=="S")and(Soledad=="S")):
    print("Felicidades Sr(a) ",Nombre, "Tienes novia y la quieres ")
if((novia=="S")and(Soledad=="N")):
    print("Sr(a) ",Nombre, "Tienes novia pero No la quieres ")
if((novia=="N")and(Soledad=="N")):
    print("Sr(a) ",Nombre, "Tienes no tienes novia(o) y estas solo te jodiste lol ")
if((novia=="N")and(Soledad=="S")):
    print("Sr(a)",Nombre," deberias decirle lo que sientes quizas se enamore de ti")

