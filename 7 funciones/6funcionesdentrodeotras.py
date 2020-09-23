# def getNombre(nombre):
#     texto=f"el nombre es: {nombre}"
#     rmbda
# eturn texto
# def getApellidos(apellidos):
#     texto=f"Los apellidos son: {apellidos}"
#     return texto

# print(getNombre("jiren"),getApellidos("suarez"))

# def devuelveTodo(nombre, apellidos):
#     texto=f"{getNombre(nombre)} \n{getApellidos(apellidos)}"
#     return texto

# print(devuelveTodo("kakaroto","suarez"))

# funcion lambda //funcion anonima que no requiere renombrarla como def 
dime_el_ano=lambda year:f"el año es: {year*50}"

print(dime_el_ano(2021))