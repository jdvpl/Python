# parametros opcionales
# cuando no se pasa parametros uno o varios parametros parametros por defecto

def getEmpleado(nombre,ID="10111111"):
    print("Empleado")
    print(f"Nombre: {nombre}")
    if ID !=None:
        print(f"Cedula: {ID}")
getEmpleado("Juan Daniel Suarez","1077870326")
getEmpleado("kakaroto",None)
getEmpleado("Jiren")