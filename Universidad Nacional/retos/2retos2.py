"""
El Centro Comercial Unaleño continúa trabajando en la creación de un carrito de compras. Para esto se requiere la creación de varias tareas que deben programarse en funciones detalladas a continuación:

Lectura de n artículos

    Se requiere leer una cantidad n de artículos que representan la compra de un cliente.
    Un artículo por ahora lleva nombre y precio.
    Esta función debe retornar la tirilla de compras en texto

Cálculo de descuento

    Dado el valor total de la compra se pretende realizar una nueva campaña titulada compra más y gasta menos con los siguientes descuentos:
        Por compras mayores a 150000 lleva un 10% de descuento.
        Por compras mayores a 300000 lleva un 15% de descuento.
        Por compras mayores a 700000 lleva un 20% de descuento.

Dadas las dos funcionalidades anteriores ayude al centro comercial a generar una tirilla de compra donde se muestren los productos comprados, el valor a pagar y el descuento que se le hizo al cliente.

Entrada: Diferentes datos en el siguiente orden:

    La cantidad de artículos en el carrito
    El nombre y el precio de cada artículo en una línea diferente

Salida: Se debe mostrar lo siguiente:

    La tirilla de compra en el formato especificado

Nota: Como el centro comercial está siendo muy generoso con los descuentos, el valor a cobrar en caso de tener centavos se debe aproximar a techo usando la función ceil de python (https://www.tutorialspoint.com/python/number_ceil.htm)

Ejemplo 1:

Entrada
	

Salida

3
Chocolatinas Cohete
300
Mora
1000
Pan de Maiz
300
# salida
Centro Comercial Unaleño
Compra más y Gasta Menos
NIT: 899.999.063
Chocolatinas Cohete $300
Mora $1000
Pan de Maiz $300
Total: $1600
En esta compra tu descuento fue $0
Gracias por tu compra
"""
import math

print("##########Tienda unaleña -Tirilla de Compra y Descuento #######".center(50))

cantidad=int(input("Ingrese la cantidad de productos "))

suma=0
nombres=[]
total=0
precios=[]
for contador in range(cantidad):
    producto=input(f"Ingresa el producto #{contador}: ")
    precio=float(input(f"Precion "))
    precios.append(precio)
    total+=precio
    nombres.append(producto)

if total > 150000 and total<=300000:
    descuento=total*0.1
    pago=total-descuento
elif total>300000 and total<=700000:
    descuento=total-total*0.15
    pago=total-descuento
elif total>700000:
    descuento=total*0.2
    pago=total-descuento
else:
    descuento=total*0
    pago=total-descuento

print("Centro Comercial Unaleño")
print("Compra más y Gasta Menos")
print("NIT: 899.999.063")

for x in range(len(nombres)):
    print(f"{nombres[x]} $ {int(precios[x])}")

print(f"Total: {math.ceil(pago)}")
print(f"En esta compra tu descuento fue ${int(descuento)}")
print("Gracias por tu compra")
    
