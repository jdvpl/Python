"""
programa de numeros pares que haya entre dos numero que elija en usuario

"""
limite_ini=int(input("Ingrese el limite inicial "))
limite_fi=int(input("ingrese el limite final "))
for contador in range(limite_ini,(limite_fi+1)):
    if contador%2==0:
        print(contador)