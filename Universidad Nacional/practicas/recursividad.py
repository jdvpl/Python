"""
Utilizando funciones recursivas, elabore un programa que simplifique una fracción escrita de la forma a/b.

Ejemplo 1
Entrada	Salida
6/4	3/2

"""

def main():
    while True:
        funcion.divisor = 2 # Variable estática
        numerador, denominador = input("\nIngresa los valores: ").split()
        if(int(numerador) <= 0 or int(denominador) <= 0):
            main()
        else:
            funcion(int(numerador), int(denominador))  
            
def funcion(numerador, denominador):
    
    # Realiza la división, !!importante la función float()
    r_num = float(numerador)/funcion.divisor
    r_den = float(denominador)/funcion.divisor
    

    # Se verifica si los dos resultados son de tipo entero
    # si los son, se vuelven a dividir por dos, llamando a la función,
    # pasando los resultados de las divisiones
    if(r_num.is_integer() and r_den.is_integer()):
        print(r_num,"/",r_den)
        funcion(r_num,r_den)
    else:        
        # Si el divisor es igual al numerador o al denominador, significa que
        # ya no es posible simplificar mas la fracción
        if(funcion.divisor == numerador or funcion.divisor == denominador or r_num <= 1 or r_den <= 1):
            print("La máxima expresión: ", numerador,"/",denominador)
        else:
            # Se se le suma 1 al divisor
            funcion.divisor += 1
            # Se pasa el valor INICIAL
            funcion(numerador, denominador) 
main()