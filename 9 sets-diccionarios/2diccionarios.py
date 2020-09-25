"""
es un tipo de dato que almacena un conjunto de datos
formato clave > valor
es lo mismo que un array con en json
"""

# persona={
#     "nombre":"Juan",
#     "apellidos":"Suarez",
#     "web":"jdvpl.com"
# }
# print(type(persona)) #tipo de dato
# print(persona) #imprime todo
# print(f" la Web: {persona['web']}") #saca los datos segun el indice

# combinan lista con diccionario

contacto=[
    {
        "nombre":"Juan Daniel",
        "Telefono":"3209188638",
        "direccion":"cr 69 #64a-19"
    },
    {
        "nombre":"Kakaroto",
        "direccion":"universo 7"
    },
    {
        "nombre":"saitama",
        "telefono":"0000000"
    }

]
print(type(contacto))
print(contacto)
print(contacto[0]["nombre"])

# modificando datos de la clave

contacto[0]["nombre"]="Natsu"
print(contacto)
print(contacto[0]["nombre"])

# recorriendo los datos con un for

for i in contacto:
    # print(i) #imprime todos los datos del diccionario
    print(f"\nNombre: {i['nombre']}")
    try:  #sino no tiene algo dentro del diccionario colocamos un try
        print(f"Direccion: {i['direccion']}")
    except:
        print("")
        # print(f"Nombre: {i['nombre']} : No tiene Direccion ")
    print("-----------------------------------")