from coche import Coche

carro=Coche(input("Color: "),input("Marca: "),input("Modelo: "),int(input("Velocidad: ")),int(input("caballaje: ")),input("Plazas: "))
carro1=Coche("Azul","vintage",2020,300,400,4)
carro2=Coche("gris","mercedes",2020,500,400,4)
print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())

# detectar tipado
if type(carro2)==Coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto")

# visibilidad public o private en la clase
print(carro.getPrivado())
print(carro1.rapido)