def main():
    entero = int(input("Ingrese un numero entero:"))
    bandera=True
    #opcion 1
    while(entero<3 or entero>90):
        entero = int(input("Ingrese un numero entero:"))

    # opcion 2
    while not (3<=entero and 90 >=entero ):
        entero = int(input("Ingrese un numero entero:"))

    print("Su número corresponde a: ", chr(entero) )
main()