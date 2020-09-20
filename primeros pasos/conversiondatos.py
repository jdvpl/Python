#para convertir a otro tipo de dato se le antepone
#la plabra reservada del tipo de dato a cual se le va a convertir
#str int flota ejemple: numero=int(25) --> aca lo comviertee a entero

texto="Jiren"
numero=25
jiren=float(numero)
kaka=str(jiren)
print(f"{texto} tiene {numero} perros") #conesta funcion no importa el tipo de dato lo imprime

print(texto+" "+str(numero))
print(jiren)
print(type(jiren))
print(kaka)
print(type(kaka))

#strings variables structura mostrando comillas en el print
#para colocar comillas dentro de un string seria 1 comenzando con comillas doble y el texto en comillas simples o viceversa
#la otra es con las barras inclinadas
mi_texto="jiren"
texto_2="es una kisama"
texto_comillas="es del \"universo 11\" " #se coloca barra inclinada 
texto_unido=(f"{mi_texto} {texto_2}")#se puede asi o con el mas es mas bonita esta forma
print(texto_unido)
print(f"{mi_texto} \n{texto_2}") #salto de linea
print(f"{mi_texto} \t{texto_2}") #espacio grande tabulacion
print(f"{mi_texto} \r{texto_2}") #borra todo lo anterior del \r