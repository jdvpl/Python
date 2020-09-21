# # el el while se controla el contador y con una condicion
# """
# es una estructura de control que repite la ejecucion de una serie de instrucciones
# tantas veces como sea necesario hasta que se deje de cumplir la condicion
# es importante que haya un contadores
# contador=0

# while condicion:
#     bloque de instrucciones
#     actualizacion de contador

# """
# contador=1
# while contador<=100:
#     print(f"Este es el numero: {contador}")
#     contador+=1


# #con comas
# print("\n\n\n\n")
# contador=1
# muestrame=str(0)
# while contador<=100:
#     muestrame=muestrame+", "+str(contador)
#     contador+=1

# print(muestrame) 
numero=int(input("numero de la tabla "))

if numero<1:
    numero=1
print(f"##### Tabla del {numero} ####")
contador=1
while contador<=10:
    print(f"{numero} x {contador} = {numero*contador}")
    contador+=1
else:
    print("Tabla terminada")    

