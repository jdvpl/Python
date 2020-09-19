#amor y amistad
print("#############################################".center(50))
print("Quieres saber si estas enamorado?".center(50))
print("#############################################".center(50))
Nombre=input("Escribe tu nombre")
Edad=int(input("Escirbe tu edad"))
Soledad=input("Vives solo? \nS (Si) \nN (no)\n")
while not (Soledad=="N")or(Soledad=="S") or  (Soledad=="n")or(Soledad=="s"):
    print("Opcion Incorrecta")
    Soledad=input("Vives solo? \nS (Si) \nN (no)\n")
print("Felicidades")
