"""
crear un escrib los numeros pares del 1 al 120

"""
# con el while
contador=0
while contador<=120:
    if contador%2==0:
        print(contador, end=",")
    contador+=1

#con el for
contador=1
for contador in range(1,121):
    if contador%2==0:
        print(f"{contador} es par")
    else:
        print(f"{contador} es impar".center(100))