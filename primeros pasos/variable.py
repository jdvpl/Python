# """ variables es un contenedor de informacion que 
#     luego puede ser aprovechada
# """

# creando variables
texto="Master en Python"
texto2="Voy a ser un full stack developer"
num=3
num2=5
print(texto)
print(texto2)
print(num)
print(num2)
print("##########################".center(50))
print("Cambia las variables".center(50))
num=25
num2=36
print(num)
print(num2)

# concatenacion
nombre="Juan Daniel Suarez"
Profesion="Full Stack Developer"
Web="Jdvpl.com"
edad=25
# con el mas identifica tipod de datos y no deja espacio
print("Nombre: "+nombre+ " es un "+ Profesion+ " y su Sitio web es: "+Web)
#con la coma no identifica el tipo de dato y deja el espacio es mejor
print("Nombre",nombre,"es",Profesion,"Su sitio web es",Web)
#interpolacion concatenacion avanzada
print("Concatenacion avanzada formateando texto")
print(f"{nombre} tiene {edad} años y es un {Profesion} -Web: {Web}".center(100))

# Concatenacion con el metodo format pasa las variables dentro del format
print("Hola me llamo {} soy un {} y mi web es: {}".format(nombre,Profesion,Web))