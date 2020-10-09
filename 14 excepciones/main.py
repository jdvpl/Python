from pprint import pprint
# capturar excepciones y manejar errores
try:
    nombre=input("Nombre:  ")

    if len(nombre)>1:
        nombre2=f"el nombre es: {nombre}"
    print(nombre2)
except:
    print("El nombre esta vacio ")
else:
    print("Excelente ")
finally:
    pprint("todo ya paso")