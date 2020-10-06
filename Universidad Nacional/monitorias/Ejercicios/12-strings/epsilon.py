'''
2. Diseñar una función que permita calcular el épsilon de la máquina. 
El épsilon de máquina es el número decimal más pequeño que sumado a 1 
se puede representar de manera precisa en la máquina (que no es redondeado), 
es decir, retorna un valor diferente de 1, éste da una idea de la precisión 
o número de cifras reales que pueden ser almacenadas en la máquina. 
La idea es realizar un ciclo en el cual se realiza la operación 1 + e para 
potencias de 2 desde e = 2^0 y continuando con potencias decrecientes de 
2 e = 2^−1, e = 2^−2, e = 2^−3, e = 2^−4, . . .
hasta obtener que el resultado de la suma 1 + e no se altere. 
Problema 5 sesion 9
'''

def epsilon():
    potencia = 0
    epsilon = 2**potencia
    epsilon_0 = epsilon
    while(epsilon > 0):
        epsilon_0 = epsilon
        epsilon = 2**potencia
        e_mas_uno = 1 + epsilon
        potencia -= 1
    return epsilon_0

print("El minimo numero positivo", end = " ")
print("en esta maquina es:", epsilon())