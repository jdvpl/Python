def min_maquina():
    Xi = 1 # Valor inicial
    Xo = Xi
    Xi = Xo / 2
    while(Xi > 0):
        Xo = Xi
        Xi = Xo / 2
    return Xo
print("El minimo numero positivo", end = " ")
print("en esta maquina es:", min_maquina())