def descuento(cantidad, precio):
    if 5 < cantidad <= 10:
        precio = precio * 0.95
    elif 10 < cantidad <= 20:
        precio = precio * 0.90
    elif 20 < cantidad:
        precio = precio * 0.80
    return precio*cantidad

def main():
    cantidad = int(input("Digite la cantidad: "))
    precio = float(input("Digite el precio: "))
    print("Valor a pagar: ", descuento(cantidad, precio))

main()