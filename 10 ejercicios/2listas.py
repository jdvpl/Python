"""
escribir un programa que añada valores a una lista
mientra que su longitud sea menor a 120 y luego mostrar la lista
-usar while y for
"""
print("\n---------- Con el While---------------")

coleccion=[]
for i in range(0,120):
    coleccion.append(i)

for x in coleccion:
    print(x, end=" " )

print("\n---------- Con el While---------------")

numer=[]
x=0
while x<=120:
    numer.append(x)
    x+=1
print(numer)
    