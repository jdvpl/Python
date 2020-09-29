# libreria para abrir un archivo
from io import open
# para las rutas
import pathlib


# abrir archivo
ruta=str(pathlib.Path().absolute()) + "/13sistema_archivos/texto.txt"
print(ruta)
# abre el archibo
archivo=open(ruta,"a+")


# escribir en el archivo
archivo.write("******************Soy un texto metidos desde python kisamado*********\n")
# cerrar archivo
archivo.close()
