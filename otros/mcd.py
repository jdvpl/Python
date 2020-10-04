
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

print(mcd(1550,12))