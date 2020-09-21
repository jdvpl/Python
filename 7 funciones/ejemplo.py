def Tabla(num):
    print(f"####Tabla del {num} ###".center(50))
    for contador in range(11):
        operacion=num*contador
        print(f"{num} x {contador} = {operacion}")
    print("\n")
numero=int(input("tabla del: "))
Tabla(numero)
    
for numero_tabla in range(1,numero+1):
    Tabla(numero_tabla)