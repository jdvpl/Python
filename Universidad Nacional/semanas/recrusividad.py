# factorial\
# para que no exceda el numero de recursion
import sys

sys.setrecursionlimit(50000)

def main(num):
    if num==1:
        return 1
    else:
        return num*main(num-1)
numero=int(input("Ingrese el numero a calcular el facotial: "))
print(main(numero))