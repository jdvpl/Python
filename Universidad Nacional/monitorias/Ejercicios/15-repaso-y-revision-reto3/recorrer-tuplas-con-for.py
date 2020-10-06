"""
2-Oct-2020 12:00
Respuesta a las preguntas de los estudiantes:
Jorge Mario Arrieta y Jhon Mario Arias.
Se aclara que lo que se muestra acá no hace parte del contenido
del módulo 1 del curso de programación. Esta es una función
avanzada.
"""
def tupla():
    tupla1 = (1,2)
    tupla2 = (2,3)
    tupla3 = (3,4)
    for i in range(1,4):
        print(locals()['tupla' + str(i)])

tupla()