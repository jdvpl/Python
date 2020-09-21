"""
las tablas de multiplicar

"""
limite=int(input("Ingresa hasta que tabla quieres mostrar "))
for nombre in range(1,(limite+1)):
    print("########################################".center(50))
    print(f"Tabla del {nombre}".center(50))
    print("########################################".center(50))
    for numero in range(1,(limite+1)):
        print(f"{numero} x {nombre} = {numero*nombre}")
    print("\n")