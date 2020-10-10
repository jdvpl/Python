import os
import pathlib
bandera=True
while bandera:
    try:
        nombre=input("Introduce el nombre: ")
        edad=int(input("edad: "))
        if edad<5or edad>110:
            raise ValueError("La edad introducida no es real")
        elif len(nombre)<1:
            raise ValueError("Ingrese un nombre correcto: ")
        else:
            print("Bienvenido al master en python ",nombre)
            bandera=False
    except ValueError:
        print("Introduce los datos correctamente\n")
    except Exception as e:
        print(f"Existe un error")

s=input("Deseas ver el directorio? ")
if s=="s" or s=="S":
    direcctorio=os.listdir("./14 excepciones")
    for i in direcctorio:
        print(i)
else:
    print(f"Gracias por estar aqui! {nombre}")