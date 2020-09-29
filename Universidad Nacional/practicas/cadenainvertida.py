def main(stri1,strin2):
    lista1=[]
    lista2=[]
    for x in stri1:
        lista1.append(x)
    lista1.reverse()
    for y in stri2:
        lista2.append(y)
    if lista1==lista2:
        return ("SI")
    else:
        return ("NO")
    return lista1
    return lista2
    
stri1=input("ingrese texto al derecho ")
stri2=input("ingrese el texto al reves: ")

print(main(stri1,stri2))
