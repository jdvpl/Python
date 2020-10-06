def por_algo(numero, mul):
    return numero*mul

#numeros_cadena = [1, 2, 3]
mul = [2, 2, 2]
numeros_cadena = ["Ironman", "Spiderman", "Ant-man", "Hulk"]
numeros_cadena
numeros = map(por_algo, numeros_cadena, mul)
numeros
t = tuple(numeros) # digite 1 2 3
print(t)

