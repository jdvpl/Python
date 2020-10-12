# programacion orientada a objetos

# definir una clase (monde para crar mas objetos de ese tipo)
# coche con caracteristicas similares

class Coche:
    # atributos o propiedades de la clase
    # caracteristicas del coche
    color="Negro"
    marca="Ferrari"
    modelo="Aventador"
    velocidad=300
    caballaje=500
    plazas=2
    # metodos que hace el objeto
    
    def setColor(self,color): #metodo set para colocarle un dato a este auto
        self.color=color
    def getColor(self):
        return self.color
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca
    def setModelo(self,modelo):
        self.modelo=modelo
    def getModelo(self):
        return self.modelo
    def setVelocidad(self,velocidad):
        self.velocidad=velocidad    
    def getVelocidad(self):
        return self.velocidad

    def acelerar(self):
        self.velocidad+=1
    def frenar(self):
        self.velocidad-=1
 

# fin definicion clase
# uso de la clase/instanciarla


print("-----------------Coche 2-------------------------")
coche=Coche()
coche.setColor(input(f"Indique el color del {coche.marca}: "))
coche.setModelo(input(f"Indique el modelo del {coche.marca}: "))

print(f"""El coche {coche.marca} Color: {coche.getColor()} modelo: {coche.getModelo()} tiene una velocidad
de: {coche.velocidad} una aceleracion de {coche.getVelocidad()}\n""")

print(f"""La velocidad actual es: {coche.getVelocidad()}""")
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
print(f"""La velocidad nueva es: {coche.getVelocidad()}""")

# creando otro objeto
print("-----------------Coche 2-------------------------")
coche2=Coche()
coche2.setMarca(input(f"Indique la marcar: "))
coche2.setColor(input(f"Indique el color del {coche2.getMarca()}: "))
coche2.setVelocidad(int(input(f"Indique la velocidad inicial del {coche2.getMarca()}: ")))

print(f"""El coche {coche2.marca} Color: {coche2.getColor()} 
modelo: {coche2.getModelo()} tiene una velocidad de: {coche2.getVelocidad()}""")
coche2.acelerar()
coche2.acelerar()
print(f"Velocidad final de: {coche2.getVelocidad()}")