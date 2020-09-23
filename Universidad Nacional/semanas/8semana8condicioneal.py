"""
Leer 4 valores enteros A, B, C y D. Si B es mayor que C y D es mayor que A y si la suma de C y D es mayor que la suma de A y B y si C y D fueran valores positivos y si A es par, escriba el mensaje “Valores aceptados” sin comilas. De lo contrario, escriba el mensaje “Valores no aceptados” sin comillas.

Entrada

La entrada corresponde a 4 valores enteros

Salida

En la salida se debe mostrar las palabras "Valores aceptados" ó "Valores no aceptados" sin comillas dependiendo de si cumplen el criterio o no.

Ejemplo 1:

Entrada                 	Salida           
5
6                           Valores no aceptados
7
8	            

"""
A=int(input("Digita el valor 1 "))
B=int(input("Digita el valor 1 "))
C=int(input("Digita el valor 1 "))
D=int(input("Digita el valor 1 "))

if B>C and D>A and (C+D)>(A+B) and C>=0 and D>=0 and D%2==0:
    print("Valores Aceptados")
else:
    print("Valores no aceptados ")