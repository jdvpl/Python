"""
calcular el cuadrado de los primeros 60 numeros

"""
#while

contador=0
while contador<=60:
    print(f"el cuadrado de {contador} es: {contador**2}")
    contador+=1
#for
print("\n\n\n\n########## con el for###############")
for contador in range(61):
    print(f"el cuadrado de {contador} es: {contador**2}")