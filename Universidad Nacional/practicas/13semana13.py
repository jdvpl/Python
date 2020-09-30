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
p=tuple(map(float,input("Digite con espacion entre ellos: ").split(" ")))
q=tuple(map(float,input("Digite con espacion entre ellos: ").split(" ")))

x,y,z=[q[i]-p[i] for i in range(3)]
distancia=math.sqrt(x**2+y**2+z**2)
print(distancia)