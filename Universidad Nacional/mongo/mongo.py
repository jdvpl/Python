# ! importando la libreria para mongodb
# !https://www.youtube.com/watch?v=pJO5gKxzsco importante ver este tutoriol
from pymongo import MongoClient

cliente=MongoClient('localhost')
# *muetra las bases de datos que hay creadas
db=cliente['prueba']
col=db['personas']
# insertar un documento en mongo

def diccionarios(nom,ed,len,hobb):
    dicccionario={}
    dicccionario['nombre']=nom
    dicccionario['edad']=ed
    dicccionario['lenguajes']=len
    dicccionario['hobbies']=hobb
    return dicccionario

# preguntando el primera diccionario
nombre=input("Ingrese el nombre: ")
edad=int(input("Ingrese la edad: "))
lenguajes=input("Ingresa los lenguajes separados por una ',': ").split(",")
hobbies=input("Ingresa tus hobbies separados por una ',': ").split(",")

# preguntando el segundo diccionario
nombre1=input("Ingrese el nombre: ")
edad1=int(input("Ingrese la edad: "))
lenguajes1=input("Ingresa los lenguajes separados por una ',': ").split(",")
hobbies1=input("Ingresa tus hobbies separados por una ',': ").split(",")

#!insertando varios documentos a la base de datos
# print([diccionarios(nombre,edad,lenguajes,hobbies),diccionarios(nombre1,edad1,lenguajes1,hobbies1)])
col.insert_many([diccionarios(nombre,edad,lenguajes,hobbies),diccionarios(nombre1,edad1,lenguajes1,hobbies1)])

# para saber cuantos documentos hay en la coleccion
print(col.count_documents({}))
