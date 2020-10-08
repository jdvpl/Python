from io import open

archivo=open("archivos/sempo.txt","a+") #creando un archivo

cuantas=int(input("Cuantas veces quieres escribir "))

for i in range(1,cuantas+1):
    lol=input("escribre algo en el archivo: ")
    archivo.write(f"{lol}\n")
    

archivo.close()

lols=open("archivos/sempo.txt","r+")
texto=lols.readlines()
for s in texto:
    print(s,end="")





