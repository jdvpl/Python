# programacion orientada a objetos

# definir una clase (monde para crar mas objetos de ese tipo)
# coche con caracteristicas similares

class Coche:
    # atributos o propiedades de la clase
    # caracteristicas del coche
    color="Negro"
    marca="Ferrario"
    modelo="Aventador"
    velocidad=300
    caballaje=500
    plazas=2
    # metodos que hace el objeto

    def acelerar(self):
        self.velocidad+=1
    def frenar(self):
        self.velocidad-=1
    def getVelocidad(self):
        return self.velocidad

# fin definicion clase
# uso de la clase/instanciarla

coche=Coche()
print(f"""El coche {coche.marca} modelo: {coche.modelo} tiene una velocidad
de: {coche.velocidad} una aceleracion de {coche.acelerar()}\n""")
print(f"""La velocidad actual es: {coche.velocidad}""")
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
print(f"""La velocidad nueva es: {coche.velocidad}""")