"""
A partir del día 1, el país A tiene una población contagiada de Divoc 9012 de n (1 <=n <= 10^8) y el país B tiene una población contagiada de Divoc 9012 de m (1 <= m <= n). Las tasas de crecimiento diario son de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que día la población contagiada del país B supera a la del país A.
Entrada
La entrada consta de dos números reales que representan la cantidad de gente contagiada.

Salida
El día en el cual la población contagiada del país B supera la del país A

"""
import math

while True:
    try:
        n=int(input("Ingresa la cantidad de infectados del pais A "))
        if(n<=100000000 and n>0):
            break
    except ValueError:
        print("El valor es incorrecto, debes ingresar un numero ")

while True:
    try:
        m=int(input("Ingresa la cantidad de infectados del pais B "))
        if(n>=m and m>0):
            break
    except ValueError:
        print("El valor es incorrecto, debes ingresar un numero ")
totalm=0
totaln=0
contador=1
while True:
    totaln=n*(1+0.02)**contador
    totalm=m*(1+0.03)**contador
    if totalm>totaln:
        break
    contador+=1
# dia=(math.log10(totalm/m))/(math.log10(1+0.03))

# print(dia)
print(f"pais A: {totaln}")
print(f"pais B: {totalm}")
if n==m:
    print(contador)
else:
    print(contador+1)


# if n==m:
#     print(f"El pais B los supera en el {dia} dia")
# else:
#     print(f"El pais B lo supera el {int(dia+1)} dia")


    