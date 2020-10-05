"""
La cercaEnunciadoUn campesino de la regi ́on le 
pide crear un programa de computador quele permita determinar 
cu ́al de dos opciones (madera o alambre) es la mejoropci ́on (menor costo)
 para encerrar un terreno rectangular den∗mmetroscuadrados, sabiendo el 
 costo de un metro lineal de alambre, el costo de unmetro de madera y la 
 cantidad de hilos de alambre o hileras de madera.  
 Elcampesino s ́olo piensa en usar una de las dos opciones, no las 
 piensacombinar.La cercaEnunciadoUn campesino de la regi ́on le pide crear 
 un programa de computador quele permita determinar cu ́al de dos opciones 
 (madera o alambre) es la mejoropci ́on (menor costo) para encerrar un 
 terreno rectangular den∗mmetroscuadrados, sabiendo el costo de un metro 
 lineal de alambre, el costo de unmetro de madera y la cantidad de hilos 
 de alambre o hileras de madera.  Elcampesino s ́olo piensa en usar una de 
 las dos opciones, no las piensacombinar.

"""
def perimetro(n,m):
    return 2*n+2*m

def en_madera(n,m,w,p):
    return perimetro(n,m) *w*p

def en_alambre(n,m,h,a):
    return perimetro(n,m)*h*a

def usar(n,m,h,a,w,p):
    if en_madera(n,m,w,p) <=en_alambre(n,m,h,a):
        return f'Madera vale \n${en_madera(n,m,w,p)}'
    else:
        return f'Alambre vale: \n${en_alambre(n,m,h,a)}'

n = float(input('¿Largo terreno?: '))
m = float(input('¿Ancho terreno?: '))
a = float(input('¿Costo metro alambre?: '))
h = int(input('¿Hilos de alambre?: '))
p = float(input('¿Costo metro madera?: '))
w = int(input('¿Hileras de madera?: '))

print("Usar", usar(n, m, a, h, p, w))