# herencia es la posibilidad de compartir
# atributos y metod entre clase y que diferentes clase hereden de otras

class Persona:
    """
    nombre
    apellido
    altura
    edad
    """
    def setNombre(self,nombre):
        self.nombre=nombre
    def getNombre(self):
        return self.nombre
    def setApellidos(self,apellidos):
        self.apellidos=apellidos
    def getApellidos(self):
        return self.apellidos
    def setAltura(self,altura):
        self.altura=altura
    def getAltura(self):
        return self.altura
    def setEdad(self,edad):
        self.edad=edad
    def getEdad(self):
        return self.edad
    
    def hablar(self):
        return f"Watashi wa {self.getNombre()}, kami desu"
    def caminar(self):
        return f"{self.getNombre()} is walking"
    def dormir(self):
        return f"{self.getNombre()} is sleeping ...☻♥♠•◘○♠"



    