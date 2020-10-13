# ! importando la libreria para mongodb
# !https://www.youtube.com/watch?v=pJO5gKxzsco importante ver este tutoriol
from pymongo import MongoClient

cliente=MongoClient('localhost')
# *muetra las bases de datos que hay creadas

db=cliente['prueba']
col=db['personas']
# insertar un documento en mongo
dicccionario={}

nombre=input("Ingrese el nombre: ")
edad=int(input("Ingrese la edad: "))
lenguajes=input("Ingresa los lenguajes separados por una ',': ").split(",")
hobbies=input("Ingresa tus hobbies separados por una coma ").split(",")
dicccionario['nombre']=nombre
dicccionario['edad']=edad
dicccionario['lenguajes']=lenguajes
dicccionario['hobbies']=hobbies

col.insert_one(dicccionario)

# para saber cuantos documentos hay en la coleccion
print(col.count_documents({}))
