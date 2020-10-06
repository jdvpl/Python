# 1*conejo + 1*gallina = 50 (total_animales)
# 4*conejo + 2*gallina = 140 (total_patas)

# solucion usando el método del determinante
def sistema_gallinas_conejos(total_animales, total_patas, patas_gallina, patas_conejo):
    det = 1*patas_conejo - patas_gallina*1

    # si el sistema tiene solución
    if det != 0:
        gallinas = ((total_animales*patas_conejo)-(1*total_patas))/det
        conejos = ((1*total_patas)-(patas_gallina*total_animales))/det
        print("El numero de conejos es: ", conejos)
        print('El numero de gallinas es: ', gallinas)
    else:
        print("Lo siento")


total_animales = int(input("digite el total de animales: "))
total_patas = int(input("digite el total de patas: "))

sistema_gallinas_conejos(total_animales, total_patas, 2, 4)


