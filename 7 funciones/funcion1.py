# """
# una funcion es un conjutno de instrucciones bajo un nombre concreto que puede 
# reutilizarse incovando a la funcion tantas veces como sea necesario
# def nombredelafuncon(parametros):
#     #bloque de codigo o conjunto de funcones
# nombredelafuncion(mi_parametro)
# """
# #ejemrplo 1
# print("mi primera funcion ")
# def muestraNombre():
#     print("jdvpl")
# muestraNombre()

# pasando parametros a las funciones
print("ejemplo #2")
Nombre=input("escribe tu nombre")
edad=int(input("ingresa la edad "))
def mostrarTunombre(nombre,edad):
    if edad>=18:
        print(f"Tu nombre es: {nombre}, y eres mayor de edad")
    else:
        print(f"Tu nombre es: {nombre}, y eres un guipa jajaja")
mostrarTunombre(Nombre,edad)


#con bucles
# canti=int(input("cuantos nombres quieres "))
# conta=1
# while conta<=canti:
#     nombre1=input(f"Digite el nombre {conta} ")
#     def mostrarNombre(final):
#         print(f"Tu nombre es: {final}")
#     mostrarNombre(nombre1)
#     conta+=1