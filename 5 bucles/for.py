"""
es una estructura iteractiva que se repita varias veces
for variables in elemento iterable(lista, rango, tupas, etc., cualquier tipo de dato):
    bloque de instrucciones
"""
contador=0
for contador in range(0,5): #rango de 0 a 5
    print(f"voy por el {contador}")
#sumando los numeros del rango
print(f"Haciendo la suma de cada bucle".center(50))
contador=0
suma=0
rango=range(0,9)
for contador in rango: #rango de 0 a 5
    print(f"voy por el {contador}")
    suma+=contador
print(f"la sumatoria del bucle del rango de {rango} es: {suma}")