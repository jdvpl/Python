def doblar(numero,mul):
    return numero*mul
x=[5,8,6,4]
mul=[3,5,8,9,10]
total=map(doblar,x,mul)
t=tuple(total)
print(t)