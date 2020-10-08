import os

# crear una carpeta
carpeta=os.path.abspath("./13sistema_archivos")
carpeta_nueva="\micarpeta"
print(carpeta+carpeta_nueva)
if not os.path.isdir(carpeta+carpeta_nueva):
    os.mkdir(carpeta+carpeta_nueva)
else:
    print("ya existe")