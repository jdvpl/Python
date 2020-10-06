x = input("ingrese la primera oración: ")
y = input("ingrese la oración invertida: ")
x1= x[::-1]
#print(x1)

if y != x1:
    print("NO")
else:
    print("SI")