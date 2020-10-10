
lista=[10,5,9,64,0,1,2,6,2,'fff']

def convertir_String(str1):
    try:
        str1=int(str1)
        return str1
    except ValueError:
        return str1

intodu=input("Introduce el numero a buscar: ")

try:
    search=lista.index(convertir_String(intodu))
    print(f"el numero {intodu} esta en la lista su indice es: {search}")

except ValueError:
    print("noooo")

# multiples excepciones
try:
    numero=int(input("Numero para elevar al cuadrado: "))
    print(f"el numero es {numero*numero}")
# except TypeError:
#     print("Debes convertirlo a int")
except ValueError:
    print("introduce un numero correcto")
except Exception as e:
    print("Ha ocurrido un error y es: ",type(e).__name__)