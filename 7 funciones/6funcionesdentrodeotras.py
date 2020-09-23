def getNombre(nombre):
    texto=f"el nombre es: {nombre}"
    return texto
def getApellidos(apellidos):
    texto=f"Los apellidos son: {apellidos}"
    return texto

print(getNombre("jiren"),getApellidos("suarez"))

def devuelveTodo(nombre, apellidos):
    texto=f"{getNombre(nombre)} \n{getApellidos(apellidos)}"
    return texto

print(devuelveTodo("kakaroto","suarez"))