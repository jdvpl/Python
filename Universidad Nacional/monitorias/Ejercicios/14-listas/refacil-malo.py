"""
ATENCION:
Esta version está errada. No soluciona el problema correctamente.
Se publica esta versión con el ánimo de que los estudiantes interesados comparen las diferencias entre
la solución correcta y esta.
"""
def datos():
    n = int(input("Ingrese numero de encuestados: "))
    opiniones = input("Ingrese opiniones. Recuerde separar con espacios \n 1 es difícil y 0 es fácil: ")
    opiniones_list = opiniones.split(" ")
    return n, opiniones_list

def analizar_opiniones(n, opiniones_list):
    while not (n == len(opiniones_list)):
        for x in opiniones_list:
            if (x != '0' or x != '1'):
                print("Los datos ingresados deben ser iguales al número de encuestados\n y las opiniones deben expresarse en 1 o 0")
                n, opiniones_list = datos()
                break

    if '1' in opiniones_list:
        print("DIFICIL")
    else:
        print("FACIL")
    
def main():
    n, opiniones_list = datos()
    analizar_opiniones(n, opiniones_list)

main()