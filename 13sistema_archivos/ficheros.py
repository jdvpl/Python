# libreria para abrir un archivo
from io import open
import shutil
# para las rutas
import pathlib
# para boraar
import os


# abrir archivo
ruta=str(pathlib.Path().absolute()) + "/13sistema_archivos/texto.txt"
# abre el archibo
archivo=open(ruta,"a+")

#escribir en un archivo
"""
# escribir en el archivo
archivo.write("******************Soy un texto metidos desde python kisamado*********\n")
# cerrar archivo
archivo.close()
"""
#copiar un archivo
"""
#copiar un archivo
ruta_original=str(pathlib.Path().absolute()) + "/13sistema_archivos/texto.txt"
ruta_nueva=str(pathlib.Path().absolute()) + "/13sistema_archivos/texto_nuevo_copiados.txt"
ruta_alternativa=str(pathlib.Path().absolute()) + "/6 ejercicios/texto_nuevo_copiados.txt"
shutil.copyfile(ruta_original,ruta_alternativa)
print(ruta_alternativa)
"""
#mover un archivo
"""
# mover un archivo lo renombra
ruta_original=str(pathlib.Path().absolute()) + "/13sistema_archivos/texto.txt"
ruta_nueva=str(pathlib.Path().absolute()) + "/13sistema_archivos/FiCHERO COPIADO.txt "

shutil.move(ruta_original,ruta_nueva)
"""
# ruta_nueva=str(pathlib.Path().absolute()) + "/13sistema_archivos/FiCHERO COPIADO.txt "
# os.remove(ruta_nueva)

ruta1=os.path.abspath("./archivos/sempo.txt")
ruta2=os.path.abspath("../")

# comprobar si existe un archivo
if os.path.isfile(ruta1):
    print("ecisladjf")
else:
    print("no existe")

archivo.close()