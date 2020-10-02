"""
ATENCION:
Esta version debe funcionar. Lo hará? :o
Cambios con respecto a refacil-malo.py:
1. En la función main(), se utiliza una bandera para que las funciones datos() y analizar_opiniones()
se corran mientras la variable bandera sea verdadera. La bandera se mantiene verdadera en dos casos:
(a) cuando los datos ingresados no corresponden al número de encuestados y (b) cuando los datos ingresados
no corresponden a '0' y '1'.
2. Como se puso el ciclo while en main, la validación de n != len(opiniones_list) debe hacerse con un condicional
if, para que en caso de ingresar en el if, se retorne al ciclo while que continuará ejecutando hasta que
el usuario ingrese la información correctamente.
3. La validación de caracteres '1' y '0' continúa haciéndose recorriendo la lista, pero se validan los caracteres
con el operador and, pues en caso de no tener NI '0' NI '1' en algún elemento, se debe terminar la validación y
regresar al ciclo while, donde se volverán a solicitar y evaluar nuevos datos ingresados por el usuario.
"""
def datos():
    n = int(input("Ingrese numero de encuestados: "))
    opiniones = input("Ingrese opiniones. Recuerde separar con espacios \n 1 es difícil y 0 es fácil: ")
    opiniones_list = opiniones.split(" ")
    return n, opiniones_list

def analizar_opiniones(n, opiniones_list):
    if (n != len(opiniones_list)):
        print("Los datos ingresados deben ser iguales al número de encuestados")
        return True

    for x in opiniones_list:
        if (x != '0' and x != '1'):
            print("Las opiniones deben expresarse en 1 o 0")
            return True

    if '1' in opiniones_list:
        print("DIFICIL")
    else:
        print("FACIL")
    return False
    
def main():
    bandera = True
    while(bandera):
        n, opiniones_list = datos()
        bandera = analizar_opiniones(n, opiniones_list)

main()