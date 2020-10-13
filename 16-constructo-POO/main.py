from coche import Coche

carro=Coche(input("Color: "),input("Marca: "),input("Modelo: "),int(input("Velocidad: ")),int(input("caballaje: ")),input("Plazas: "))
carro1=Coche("Azul","vintage",2020,300,400,4)
print(carro.getInfo())
print(carro1.getInfo())