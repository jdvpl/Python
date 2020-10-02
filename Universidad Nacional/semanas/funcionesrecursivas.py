# la suma pero sin sumar los dos numeros directamente
def h(n,m):
    if m==0:
        return n
    else:
       return h(n+1,m-1)
print(h(2,3))


# la sumatoria de los numeros por ejemplo digita 4 entonces 4+3+2+1

def sumatoria(num):
    if num==1:
        return 1
    else:
        return num+sumatoria(num-1)

numero=int(input("Figite el numero a sumar "))
print(sumatoria(numero))


# portecia

def potenciacion(b,n):
    if n==0:
        return 1
    else:
        return potenciacion(b,n-1)*b

base=int(input("Ingrese base: "))
potencia=int(input("Ingrese la suma: "))

print(potenciacion(base,potencia))

# pagos
def pagos(m,i,n):
    if n==0:
        return m
    else:
     return pagos(m,i, n-1)*(1+i)

print(pagos(5000,2,5))