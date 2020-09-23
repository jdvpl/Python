"""\

listas(arrays)
son colecciones o conjuntos de datos/valores, bajo un unico nombre
para acceder a esos valores podemos usar un indica numericos

"""
pelicula="batman"
# definir una lista
peliculas=["goku","spiderman","sr de los anillos","broly"]
# otra definicion de lista
cantantes=list(("bon jovi","metallica","michael jason","romero santos","enrique"))
# lista con rangos
anos=list(range(2020,2050))
# lista variada
variada=["kakaroto",30,25.6,False,"texo"]


# print(pelicula)
# # lista de peliculas
# print(peliculas)
# # lista de cantantes
# print(cantantes)
# # lsuita de anos
# print(anos)
# # lista variada

# reasignando valores a un indice de la lista
peliculas[2]="popeye"
# indices
print(peliculas)
print(peliculas[1])
print(peliculas[-1]) #se devuelve en el primer puesto al reves
print(cantantes[1:4]) #imprime los de la posicion 1 al 4 menos una posicion osea que comienza del 1 hasta 3
print(cantantes[1:])#todos los que hay apartir de la posicon 1
print(cantantes[:2]) #todos los anteriores a la posicion 2 osea el 0 y el 1

# añadir elementos a una lista
cantantes.append("aerosmith")
cantantes.append("linkin park")
cantantes.append("shisu kane")

print(cantantes)