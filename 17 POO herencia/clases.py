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


# here
class Programador(Persona):
    """
    lenguajes
    experiencia
    """
    def __init__(self):
        self.lenguajes="HTML, CSS JavaScript, PHP"
        self.experiencia=3

    def aprender(self,lenguajes):
        self.lenguajes=lenguajes
        return self.lenguajes

    def getLenguajes(self):
        return self.lenguajes

    def setExperiencia(self,experiencia):
        self.experiencia=experiencia
    def getExpeiencia(self):
        return self.experiencia
    
    def programar(self):
        return "Estoy programando"
    def reparar(self):
        return "He reparado tu laptop"
class TecnicoRedes(Programador):
    def __init__(self):
        # con este metodo asigna los valores de la clase padre (programador)
        super().__init__()
        self.auditarRedes='experto'
        self.experiencia=15 
    def auditoria(self):
        return "estoy auditando una red"
