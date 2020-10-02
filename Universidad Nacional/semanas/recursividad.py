"""
funciones recursivas
"""
def buscar(cadena, letra, tam):
    if tam==1:
        return cadena[0] ==letra
    else:
        return (cadena[tam-1]==letra) or buscar(cadena,letra,tam-1)

print(buscar("abc","x",len("abc")))
print(buscar("mtdcc","m",len("mtdcc")))

# funcion par con recrusividad
def par(n):
    if n==0:
        return True
    elif n==1:
        return False
    else:
        return par(n-2)

print(par(0))
print(par(1))
print(par(2))
print(par(3))
print(par(4))
print(par(5))
print(par(6))


# modulo residuo

def g(n):
    if n<3:
        return n
    else:
        return g(n-3)
    
print(g(0))
print(g(1))
print(g(2))
print(g(3))
print(g(4))
print(g(5))