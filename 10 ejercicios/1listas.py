"""
hacer un programa que tenga una lista de 8 numeros
-reccorrer la lista y mostrarla
-hacer el recorrido con una funcion 
-ordenarla y mostrarla
-mostrar su longitud
-buscar un elemento que el usario indique por teclado
"""
def recorriendo(x): # definiendo funcion que me recorra la lista
    resul="" #variable vacia para ir agregando los valores alli
    for i in x:
        resul+=f"{x.index(i)+1}: {i}" #colocandole el indice al la lista
        resul+="\n"
    return resul

lista=[1,9,7,6,8,4,3,5]

print("---------------------Lista sin la funcion -------------\n")
for i in lista:
    print(i, end=" ")


print("\n---------------------Lista con la funcion -------------\n")
print(recorriendo(lista))
# print(recorriendo(range(-2,6,2)))

print("\n---------------------Lista Ordenada -------------\n")
lista.sort()
print(recorriendo(lista))
print("\n---------------------Mostrar longitud -------------\n")
print(len(lista))
print("\n---------------------Buscar un elemento que el usuario pida por teclado -------------\n")



# con error si no ingresa un valor correcto
# busque=int(input("introduce el numero: "))
# comprpbar=isinstance(busque,int)
# while not comprpbar or busque<=0:
#     busque=int(input("introduce el numero: "))
# else:
#     print(f"Has introducido el {busque}")

# print(f"############### buscar en la lista el numero {busque} ########")

# encontrarndo=lista.index(busque)

# print(f"El numero {busque} se encuentra en la lista es el indice: {encontrarndo}")

# controlando los errores
while True: # como yo lo haria
    try:
        busque=int(input("Numero a Buscar: ")) 
        break
    except:
        print("Valor incorrecto ")

try:
    encontrarndo=lista.index(busque)
    print(f"El numero {busque} se encuentra en la lista es el indice: {encontrarndo}")
except ValueError:
    (f"El numero {busque} No se encuentra en la lista ")
    
    