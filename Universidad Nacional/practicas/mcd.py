
# maximos comun divisor

def mcd(a,b):
    minimo=min(a,b)
    maximos=max(a,b)

    if minimo==0:
        return maximos
    elif minimo==1:
        return 1
    else:
        return mcd(minimo,maximos%minimo)

# def main():


amplificado=input("ingrese numero '/':")
numerador,denominador=amplificado.split("/")
a=int(numerador)
b=int(denominador)

x=a/mcd(a,b)
y=b/mcd(a,b)

print(f"{int(x)}/{int(y)}")

print(mcd(a,b))