"""
Utilizando tuplas elabore un método que retorne la distancia entre dos puntos 𝑝 y 𝑞 definidos en un espacio de 3 dimensiones:

La distancia corresponde a aplicar: d igual raíz cuadrada de paréntesis izquierdo x subíndice 2 menos x subíndice 1 paréntesis derecho al cuadrado más paréntesis izquierdo y subíndice 2 menos y subíndice 1 paréntesis derecho al cuadrado más paréntesis izquierdo z subíndice 2 menos z subíndice 1 paréntesis derecho al cuadrado fin raíz

Entrada

La entrada corresponde a los valores de cada una de las coordenadas x, y, z de cada punto:
Salida

Un único valor correspondiente a la distancia entre los dos puntos.

Para una mayor referencia puede consultar distancias en el espacio

"""
import math
numero1=input("Ingrese los puntos de p ")
n1,x1,p1=numero1.split(" ")
numero2=input("Ingrese los puntos de q ")
n2,x2,p2=numero2.split(" ")
distancia=math.sqrt((int(n1)-int(n2))**2+(int(x1)-int(x2))**2+(int(p1)-int(p2))**2)
print(distancia)