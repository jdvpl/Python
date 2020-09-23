# def saludame(nombre="Juan"):
#     saludo=f"Hola saludos {nombre}"
#     return saludo #devuelve el saludo
# print(saludame("kakaroto"))
# ejemplo completo calculadora
def calculadora(n1,n2,basicos=False):
    suma=n1+n2
    resta=n1-n2
    multi=n1*n2
    divi=n1/n2

    cadena=""
    if basicos !=False:
        print("\nOperaciones Basicas: ")
        cadena+=f"Suma: {suma}"
        cadena+="\n"
        cadena+=f"Resta: {resta}"
        cadena+="\n"
    else:
        print("\n complejas: ")
        cadena+=f"Multiplicacion: {multi}"
        cadena+="\n"
        cadena+=f"Division: {divi}"

    return cadena

print(calculadora(5,6,True))