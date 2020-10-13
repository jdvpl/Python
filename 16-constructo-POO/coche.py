class Coche:
    # atributos o propiedades de la clase
    # caracteristicas del coche
    color="Negro"
    marca="Ferrari"
    modelo="Aventador"
    velocidad=300
    caballaje=500
    plazas=2

    # definir el constructor
    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas


    # metodos que hace el objeto setters y getter
    
    def setColor(self,color): 
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
    
    # mostrar toda la info
    def getInfo(self):
        info="---------Informacion del coche --------\n"
        info+=f"\nColor: {self.getColor()}"
        info+=f"\nMarca: {self.getMarca()}"
        info+=f"\nModelo: {self.getModelo()}"
        info+=f"\nVelocidad: {self.getVelocidad()} Kh/h"
        return info