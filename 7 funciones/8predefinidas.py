#funciones predefinidas

nombre="Kakaroto suarez"
#funciones generales
print(type(nombre))

# detectar el tipado
comprobar =isinstance(nombre,str) #comprueba si es string el segundo parametro
if comprobar:
    print("es string")
else:
    print("no es un string")

if not isinstance(nombre,float):
    print("la variable no es un numero con decimales")
else:
    print("es un decimal")

    #limpirar espacios

frases= "                            mi contenido            "
print(frases)
print(frases.strip()) #limpia espacios a la derecha y a la izquierda 

# borrando las variables
# year=2025
# print(year)
# del(year)
# print(year)
# comprobar si la variable esta vacia
# funcion len cuantos caracteres tiene un string
texto="   ff  "
if len(texto)<=0:
    print("la variable esta vacia")
else:
    print(f"la variable tiene {len(texto)} caracteres")

# encontrar caracteres .find muesta en que posicion del caracter se encuentra la palabra o texot que le pases

frase="La vida es bella"
print(frase.find("s"))
# reemplazar palabras en un string
nueva_frase=frase.replace("bella","magnifica")

print(nueva_frase)

# mayusculas y minusculas conversion

print(nueva_frase.lower()) #convierte en minuscula
print(nueva_frase.upper())
print(nueva_frase.capitalize())
