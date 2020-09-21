"""
programa que muestra un rango de numeros que el usuario engresa
"""
num_inicial=int(input("Ingrese el rango inicial "))
num_final=int(input("Ingrese el rango final "))

if num_inicial < num_final:
    for contador in range((num_inicial),(num_final+1)):
        print(contador)
else:
    # while num_inicial>=num_final:
    #     print(num_inicial)
    #     num_inicial-=1
        #con el for

    print("\n\n\n\n\ncon el for")
    for contador in range(num_inicial,(num_final-1),-1):
        print(contador)
