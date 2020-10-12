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
    def setModelo(self,modelo):
        self.modelo=modelo
    def getModelo(self):
        return self.modelo
    def acelerar(self):
        self.velocidad+=1
    def frenar(self):
        self.velocidad-=1
    def getVelocidad(self):
        return self.velocidad

# fin definicion clase
# uso de la clase/instanciarla



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