"""
En esta ocasión el centro comercial tiene en formato JSON archivos con el listado de compras realizadas en internet. Dado este formato, se requiere su ayuda para que se generen las tirillas de compra que se encuentran almacenadas en un sitio determinado de internet.

El formato de tirilla es similar al del último reto.

El cálculo de descuento se mantiene y se debe generar la misma tirilla que se generó en el reto anterior. Dado el valor total de la compra se continúa con la campaña titulada compra más y gasta menos con los siguientes descuentos:

    Por compras mayores a 150000 lleva un 10% de descuento.
    Por compras mayores a 300000 lleva un 15% de descuento.
    Por compras mayores a 700000 lleva un 20% de descuento.

Entrada: Este programa tiene como entrada un enlace que corresponde al archivo json que se quiere procesar. Puede ser cualquier enlace, pero se garantiza que el archivo maneja el mismo formato del archivo de ejemplo.

Salida: Tirillas de compra de acuerdo al procesamiento del archivo de internet especificado.

Nota: Como el centro comercial está siendo muy generoso con los descuentos, el valor a cobrar en caso de tener centavos se debe aproximar a techo usando la función ceil de python (https://www.tutorialspoint.com/python/number_ceil.htm)

Ejemplo: 

Entrada: https://raw.githubusercontent.com/arleserp/MinTIC2022/master/json/comprassmall.json

"""

import json,requests,math
from pprint import pprint

def main(url):
    response=requests.get(url)
    datos=json.loads(response.text)
    suma=0
    for i in range(len(datos)):
        print("Centro Comercial Unaleño")
        print("Compra más y Gasta Menos")
        print("NIT: 899.999.063")
        cliente=datos[i]['cliente']
        productos=datos[i]['productos']
        print(f"Cliente: {cliente}")
        print(f"Art Cant Precio")
        total=[]
        for producto in range(len(productos)):
            nombre=productos[producto]['nombre']
            cantidad=int(productos[producto]['cantidad'])
            precio=int(productos[producto]['precio unitario'])
            total.append(precio*cantidad)
            print(f"{nombre} x{cantidad} ${precio*cantidad}")
        suma=sum(total)
        if suma > 150000 and suma<=300000:
            descuento=suma*0.1
            pago=suma-descuento
        elif suma>300000 and suma<=700000:
            descuento=suma*0.15
            pago=suma-descuento
        elif suma>700000:
            descuento=suma*0.2
            pago=suma-descuento
        else:
            descuento=suma*0
            pago=suma-descuento
        print(f"Total: {math.ceil(pago)}")
        print(f"En esta compra tu descuento fue ${int(descuento)}")
        print("Gracias por tu compra")
        print("---")

url=input("Ingrese la url del json: ")
main(url)
