import os,shutil
from io import open

# crear una carpeta
carpeta=os.path.abspath("./13sistema_archivos")
carpeta_nueva=input("Digite el nombre de la carpeta a crear: ")
cosito="\\"
print(carpeta+cosito+carpeta_nueva)
if not os.path.isdir(carpeta+cosito+carpeta_nueva):
    os.mkdir(carpeta+cosito+carpeta_nueva)
else:
    print("ya existe")


# eliminar directorio
try:
    cual=input("Cual carpeta deseas eliminar: ")
    os.rmdir(carpeta+cosito+cual)
except:
    print("la carpeta no existe")

"""
# copiar directorios
ruta_original=os.path.abspath("./13sistema_archivos/micarpeta")
ruta_nueva=os.path.abspath("./13sistema_archivos/micarpeta_COPIADA")

shutil.copytree(ruta_original,ruta_nueva)
"""
""" agregando archvos por medi ode la consola
nombre_archivo=input("indique el nombre del archivo con la extension: ")
ruta=os.path.abspath("./archivos/"+nombre_archivo)
archivo=open(ruta,"a+")
archivo.write(f"Hola insecto creando el archivo: {nombre_archivo} ")
print(ruta)
"""

print("\nContenido de la Carpeta: \n")
contenido=os.listdir("./13sistema_archivos")
for con in contenido:
    print(con)
print()

ver=input("Ver el contenido de la carpeta: ")
ver2=os.listdir("./13sistema_archivos/"+ver)
for ss in ver2:
    print(ss)
    
capeta_vieja=input("nombre de la carpeta a mover: ")
ruta_original=os.path.abspath("./13sistema_archivos/"+capeta_vieja)
nombre_caprte=input("Indique el nombre de la carpeta: ")
ruta_nueva=os.path.abspath("./13sistema_archivos/"+nombre_caprte)
# renombrando carpeta
shutil.move(ruta_original,ruta_nueva)

