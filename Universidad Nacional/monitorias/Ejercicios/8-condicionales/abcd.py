"""
Leer 4 valores enteros A, B, C y D. 
*Si B es mayor que C 
*y 
*D es mayor que A 
*y 
*si la suma de C y D es mayor que la suma de A y B 
*y 
*si C y D fueran valores positivos 
*y 
*si A es par
, escriba el mensaje “Valores aceptados”. 
De lo contrario, 
escriba el mensaje “Valores no aceptados”.
"""
def ejercicio_if():
    a = int(input("Ingrese el valor de A: "))
    b = int(input("Ingrese el valor de B: "))
    c = int(input("Ingrese el valor de C: "))
    d = int(input("Ingrese el valor de D: "))

    if (b>c and d>a and c+d > a+b and c>=0 and d>=0 and a%2 == 0):
        print("Valores aceptados")
    else:
        print("Valores no aceptados")

ejercicio_if()
