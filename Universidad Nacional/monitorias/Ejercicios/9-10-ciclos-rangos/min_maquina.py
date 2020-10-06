def min_maquina():
    Xi = 1.0 # Valor inicial
    Xo = Xi
    Xi = Xo / 2.0
    while(Xi > 0.0):
        Xo = Xi
        Xi = Xo / 2.0
    return Xo
print("El m´ınimo n´umero positivo", end = " ")
print("en esta m´aquina es:", min_maquina())