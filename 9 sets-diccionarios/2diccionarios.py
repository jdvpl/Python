"""
es un tipo de dato que almacena un conjunto de datos
formato clave> valor
es lo mismo que un array con en json
"""

persona={
    "nombre":"Juan",
    "apellidos":"Suarez",
    "web":"jdvpl.com"
}
print(type(persona)) #tipo de dato
print(persona) #imprime todo
print(f" la Web: {persona['web']}") #saca los datos segun el indice
