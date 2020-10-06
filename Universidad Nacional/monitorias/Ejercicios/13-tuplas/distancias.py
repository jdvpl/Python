from math import sqrt
p = tuple(map(float, input("digite tres números con espacio entre ellos: ").split(' '))) 
q = tuple(map(float, input("digite tres números con espacio entre ellos: ").split(' '))) 

x2, y2, z2 = [(q[i]-p[i])**2 for i in range(3)]
d = sqrt(x2 + y2 + z2)
print(d)

#solucion alternativa
#x, y, z = [q[i]-p[i] for i in range(3)]
#d2 = (x**2 + y**2 + z**2)**(1/2)
#print(d2)