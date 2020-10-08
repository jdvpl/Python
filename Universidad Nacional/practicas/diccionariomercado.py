"""
Dory quiere ir al mercado a comprar frutas y vegetales. Como es un poco olvidadiza suele ir al mercado varias veces para ir a comprar diferentes frutas y verduras.

Entrada:

La entrada de este problema contiene un entero N que es la cantidad de viajes que hace al mercado. En cada viaje se define un número M correspondiente a la cantidad de productos disponibles en el mercado. Después se tienen M productos con sus precios respectivos por kg. La siguiente entrada contiene un entero P que indica la cantidad de productos que Dory quiere comprar. Las siguientes líneas contienen el nombre del producto y la cantidad de kilos que Dory quiere comprar.

Salida:

Muestre el dinero gastado por Dory en cada viaje al mercado con dos cifras de precisión decimal.

"""
def main():
    N=int(input("Ingrese las veces que fue al supermercado: "))
    for n in range(N):
        supermercado={}
        lista_compras={}
        n_supermercado=int(input("ingrese la cantidad de productos disponibles: "))
        for i in range(n_supermercado):
            info_producto=input()
            info_producto_lista=info_producto.split(" ")
            nombre=info_producto_lista[0]
            precio=float(info_producto_lista[1])
            supermercado[nombre]=precio

        print(supermercado)

        n_lista_conpras=int(input("Ingrese la cantidad de productos a comprar: "))
        for x in range(n_lista_conpras):
            info_producto=input()
            info_producto_lista=info_producto.split(" ")
            nombre=info_producto_lista[0]
            cantidad=int(info_producto_lista[1])
            lista_compras[nombre]=cantidad

        total=0

        for producto_actual in lista_compras:
            cantidad=lista_compras[producto_actual]
            precio=supermercado[producto_actual]
            total_producto=cantidad*precio
            total=total+total_producto
        print(f"{'{:.2f}'.format(total)}")  #para imprimir con dos decimales
main()