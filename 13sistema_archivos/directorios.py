import os,shutil

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


# copiar directorios
ruta_original=os.path.abspath("./13sistema_archivos/micarpeta")
ruta_nueva=os.path.abspath("./13sistema_archivos/micarpeta_COPIADA")

shutil.copytree(ruta_original,ruta_nueva)