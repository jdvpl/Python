color=input("Adivina mi color favorio ")
if color=="negro":
    print(f"Ese es mi color favorito el {color}")
else:
    print(f"No te fregaste insecto")
     
#operadores de compacion jejejeje
"""
== igual
!= diferente
< menor que
> mayor que
>= mayor o igual que
<= menor o igual que

"""
year=int(input("Ingrese el año "))
if year>=2020:
    print("Estamos en el 2020 o superior")
else:
    print(f"estamos en el pasado jejeje año {year}")

#if anidados
print(f"########################## if Anidados ####################")
nombre=input("Ingrese su nombre ")
ciudad=input("Ingrese la ciudad")
continete=input("Ingrese el continete donde vive")
edad=int(input("Ingrese su edad"))
if edad>=18:
    print(f"Sr {nombre} eres mayor de edad ")
    if continete!="america":
        print(f"Eres del mejor continente {continete}")
    else:
        print(f"Es americano y de la ciudad {ciudad}")
else:
    print(f"Eres un guipa jejeje")
