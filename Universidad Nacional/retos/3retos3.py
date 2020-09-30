"""
El Centro Comercial Unaleño está muy cerca de crear carrito de compras. Ahora lo que se requiere de su parte es que se puedan agregar un número indefinido de artículos y calcular la cuenta.

 Se han definido varios comandos para realizar la prueba de la lógica del carrito de compras a bajo nivel. Para esto se definen ahora diferentes comandos que se realizan al momento de realizar una compra y que presentan la siguiente sintaxis: 

comando&sintaxis_comando

 Los comandos definidos ahora son:

 Comando 1:  Añadir ítem al carrito de compras

 La sintaxis del comando 1 es la siguiente:

1&nombre_articulo&cantidad&precio

 Comando 2: Generar tirilla de compras

 La sintaxis del comando 2 es la siguiente:

2&cedula_cliente

    Esta función debe retornar la tirilla de compras en texto
    El cálculo de descuento se mantiene y se debe generar la misma tirilla que se generó en el reto anterior, pero incluyendo la cédula del cliente. Dado el valor total de la compra se continúa con la campaña titulada compra más y gasta menos con los siguientes descuentos:
            Por compras mayores a 150000 lleva un 10% de descuento.
            Por compras mayores a 300000 lleva un 15% de descuento.
            Por compras mayores a 700000 lleva un 20% de descuento
    Al imprimir la tirilla, la aplicación elimina ese carrito de compras y queda disponible para ejecutar de nuevo comandos.

Comando 3 – Salir de la aplicación

La sintaxis del comando 3 es la siguiente:

3

 Este comando simplemente permite salir de la aplicación

Entrada: Diferentes comandos según el cargue y la impresión de tirillas de venta

Salida: Salidas dependiendo del comando especificado anteriormente

Nota: Como el centro comercial está siendo muy generoso con los descuentos, el valor a cobrar en caso de tener centavos se debe aproximar a techo usando la función ceil de python (https://www.tutorialspoint.com/python/number_ceil.htm)

"""
import math

print("##########Tienda unaleña -Tirilla de Compra y Descuento #######".center(50))

def main():
    bandera=True
    factura=[]
    suma=0
    while bandera:
        datos=input("Digite el comando ")
        comando=datos.split("&")
        subfactura=[]
        total=1
        if comando[0]=="1":
            comando,nombre,cantidad,precio=datos.split("&")
            total=int(precio)*int(cantidad)
            suma+=total
            subfactura.append(nombre)
            subfactura.append(int(cantidad))
            subfactura.append(int(total))
            factura.append(subfactura)

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

            
        elif comando[0]=="2":
            comando,cedula=datos.split("&")
            print("Centro Comercial Unaleño")
            print("Compra más y Gasta Menos")
            print("NIT: 899.999.063")
            print(f"Cliente: {cedula}")
            print("Art Cant Precio")
            for x in factura:
                for elemento in x:
                    if x.index(elemento)==0:
                        print(f"{elemento} ",end="")
                    elif x.index(elemento)==1:
                        print(f"{elemento} ",end="")
                    else:
                        print(f"${elemento}")

            print(f"Total: {math.ceil(pago)}")
            print(f"En esta compra tu descuento fue ${int(descuento)}")
            print("Gracias por tu compra")
            suma=0
            factura=[]
            print("----")
            
        elif comando[0]=="3":
            bandera=False
        else:
            bandera=False
        
main()
