def main():
    entero = int(input("Ingrese un numero entero:"))
    bandera = True
    #opcion 1
    while(bandera and (entero<65 or entero>90)):
        entero = int(input("Ingrese un numero entero:"))
        bandera = False

    # opcion 2
    #while not (65<=entero and 90 >=entero ):
    #    entero = int(input("Ingrese un numero entero:"))

    print("Su número corresponde a: ", chr(entero) )
main()