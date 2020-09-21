"""
numeros indefinidos hasta que el usuario introduzca la clave
"""
contador=1
lisa=[]
while contador<100:
    numero=int(input("Para que se detenga introduzca la clave: "))

    if numero==111:
        print("Felicidades")
        break
    else:
        lisa.append(numero)
        print(f"has introducido el {numero} es incorrecta la clave jejeje")
print(f"los numeros ingresado incorrectamente fueron: {lisa}")       