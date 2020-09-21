# """
# es una estructura iteractiva que se repita varias veces
# for variables in elemento iterable(lista, rango, tupas, etc., cualquier tipo de dato):
#     bloque de instrucciones
# """
# contador=0
# for contador in range(0,5): #rango de 0 a 5
#     print(f"voy por el {contador}")
# #sumando los numeros del rango
# print(f"Haciendo la suma de cada bucle".center(50))
# contador=0
# suma=0
# rango=range(0,9)
# for contador in rango: #rango de 0 a 5
#     print(f"voy por el {contador}")
#     suma+=contador
# print(f"la sumatoria del bucle del rango de {rango} es: {suma}")

# ejemplos del bucle for
print("################tabla de multiplicar##################")
numero=int(input("Por favor indique el numero a multiplicar "))
if numero<1:
    print(f"{numero}Numero incorrecto asi que se va a tomar el valor 1")
    numero=1
print(f"####Tabla de multiplicar del numero {numero} ####")

for numero_tabla in range(1,11):

    if numero>=50: #colocando condiciones dentro del for
        print(f"El programa no muestra la tabla del {numero} solo menores a 50")
        break #para cortar el bucle solo si se cumple
    

    print(f"{numero} x {numero_tabla} = {numero*numero_tabla}")
else:
    print("###tabla finalizada")