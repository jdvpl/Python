"""
son funcionalidades ya hechas para reutilizar

https://docs.python.org/3/py-modindex.html

podemos conseguir modulos que viene en el lenguaje,
modulos en internet y podemos crear modulos
"""
#importando todos los modulos pero colocando la palabra modulo el nombre del
#archivo
# import modulo

from modulo import calculadora #solo para una funciondsa
#asi se importan todas las funciones que estan en el modulo para no 
#colocarle la palabra modulo..
from modulo import * 

# modulo fecha
import datetime

# print(modulo.saludos("Kakaroto"))
# print(modulo.calculadora(5,6,True))

print(calculadora(5,6,True))
print(saludos("Jiren"))

# imprimir la fecha de hoy
print("\n-------------fecha de hoy ------------\n")
print(datetime.date.today())

fecha_completa=datetime.datetime.now()
print("\n-------------fecha completa con hora------------\n")
print(fecha_completa)

print("\n-------------ano de hoy------------\n")
print(fecha_completa.year)
print("\n-------------mes de hoy------------\n")
print(fecha_completa.month)
print("\n-------------dia de hoy------------\n")
print(fecha_completa.day)
print("\n-------------fecha personalidada------------\n")

personalizada=fecha_completa.strftime("%d de %m del %Y, %H:%M:%S")
print(personalizada)

print("\n-------------fecha timestamp------------\n")
print(fecha_completa.now().timestamp())

print("\n-------------fecha time------------\n")
print(fecha_completa.now().times())