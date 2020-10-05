"""
Al ver los precios y los anuncios del almac ́enCobra Mosmas, un cliente lepide crear
 un programa de computador que le permita ingresar el precioindividual de tres productos
  y el precio de la promoci ́on en combo de  lostres productos anunciada por el almacen
   y determine si es preferiblecomprarlos por separado o en el combo promocion
"""
def comprar(p1,p2,p3,pc):
    if pc <=p1+p2+p3:
        return f'Combo vale ${pc}\nseparado vale ${p1+p2+p3}'
    else:
        return f'Por separado vale ${p1+p2+p3}\nEn combo: ${pc}'

a = float(input('¿Precio del primer producto?: '))
b = float(input('¿Precio del segundo producto?: '))
c = float(input('¿Precio del tercer producto?: '))
d = float(input('¿Precio del combo?: '))

print(f"Comprar {comprar(a,b,c,d)}")