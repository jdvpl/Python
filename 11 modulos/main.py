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

# print(modulo.saludos("Kakaroto"))
# print(modulo.calculadora(5,6,True))

print(calculadora(5,6,True))
print(saludos("Jiren"))