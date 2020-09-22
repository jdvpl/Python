import math
pi=math.pi
def rectangulo(a,b):
    return a*b
def circulo(r):
    return pi*r**2
    
sumaTotal=0
a1=float(input("ingrese el valor uno "))
b1=float(input("ingrese el valor dos "))
sumaTotal+=rectangulo(a1,b1)
a2=float(input("ingrese el valor uno "))
b2=float(input("ingrese el valor dos "))
sumaTotal+=rectangulo(a2,b2)
r1=float(input("ingrese el valor uno "))
sumaTotal+=circulo(r1)
r2=float(input("ingrese el valor dos "))
sumaTotal+=circulo(r2)
print(f"suma total= {sumaTotal}")
