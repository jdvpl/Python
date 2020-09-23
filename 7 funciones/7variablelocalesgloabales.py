"""
variables locales:se defines dentro de la funcion y no  se puede usar fuera de ella
solo estan disponibles dentro
a no ser que hagamos un retunr

variables globales: son las que se declaran fuera de una funcion
y estan disponibles dentro y fuera de ellas
"""
frase="jiren es un marica y no pudo vencer a kakaroto" #variable global
print(frase)
def hola():
    frase="hola mundo"
    print("dentro de la funcion")
    print(frase)

    year=2000
    print(year) #solo es accesible dentro de la funcion


    global website #hace que la variable sea global para reutilizarla por fuera de la funcion
    website='jdvpl.com'
    print(f"Dentro, {website}")

    return year

# print(website)

print(hola())
print(f"Fuera {website}")