anime=['Dragon Ball','Nanatsu no Tanzai','Akame ga Kill','Kiss x Kiss','Naruto','One Piece']

numeros=[1,3,2,6,9,10,2,4,7,11,15,12,2]
print(numeros) #lista desordenada

#ordenar la lista

numeros.sort() #para ordenar los numeros

print(numeros)
#añadir elementos a la lista

anime.append("Baki") #con este se agrega al final
print(anime)

anime.insert(4,"Boruto") #con este metodo se agrega el el indica que uno quiera
print(anime)

#eliminar elementos de la lista
anime.pop(-1)
anime.remove("Naruto") #elimina por el nombre
print(anime) #eliminar el elementos

print(numeros)
numeros.reverse() #invierte la lista
print(numeros)

print('Boruto' in anime) #para buscar algo en la lista

#contar el numero de elementos
print(anime)
print(len(anime))

#cuantas aparece un elemento para los repetidos (2)
numeros.insert(1,2)
print(numeros.count(2))
#en que indice esta un objeto

print(anime.index("Boruto"))

numeros.sort() #ordena la lista pero solo con enteros
#unir lista
anime.extend(numeros)

print(anime)