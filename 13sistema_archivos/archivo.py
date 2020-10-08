# leyendo el archivo ya hecho
# libreria para abrir un archivo
from io import open
# para las rutas
import pathlib
import shutil

# especificar ruta
ruta=str(pathlib.Path().absolute()) + "/13sistema_archivos/texto.txt"
# abre el archibo con permiso de lectura read
archivo=open(ruta,"r+")

x=input("Ingrese un texto al archivo: ")

archivo.write(f"{x}\n")
# leer contenido del archivo
# contenido=archivo.read()
# print(contenido) #muesta el contenido directamente

# for i in contenido:
#     print(i) #leer letra a letra

# otra forma de leer y guardarlo en lista

lista=archivo.readlines()
archivo.close()

print(lista)
for x in lista:
    # if not x.isnumeric(): si es numerico
    lista_frase=x.split() #para colocar cada frase o en una lista diviendolo con el espaciado
    print(lista_frase)
    print(x.upper())

ruta_alternativa=str(pathlib.Path().absolute()) + "/archivos/texto_nuevo.txt" #copiando a otra ruta
# print(ruta_alternativa)
shutil.copyfile(ruta,ruta_alternativa)
