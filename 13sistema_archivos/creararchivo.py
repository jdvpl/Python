from io import open

archivo=open("13sistema_archivos/texto.txt","a+") #creando un archivo

cuantas=int(input("Cuantas veces quieres escribier "))


for i in range(cuantas+1):
    lol=input("escribre algo en el archivo: ")
    archivo.write(f"{lol}\n") 
    texto=archivo.readlines()
    print(texto)

archivo.close()