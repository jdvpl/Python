"""
un programa que tenga 4 variables, lista, string, entero y bool
y que imprima un mensaje segun el tipo de cada variable
"""
def TraducirTipo(tipo):
    result=None
    if tipo==list:
        result="LISTA"
    elif tipo==int:
        result="ENTERO"
    elif tipo==str:
        result="CADENA"
    elif tipo==bool:
        result="BOLEANO"
    return result

def comprobarTipado(variable,tipo):
    texto=isinstance(variable,tipo)
    result=""
    if texto:
        result=f"{variable} es del tipo de dato: {TraducirTipo(tipo)}"
    else:
        result=f"No es ese tipo de dato {tipo}"
    
    return result

lista=["Hola mundo",77]
string="jiren"
numero=100
verdadero=True

print("---------------------------------------\n")
print(comprobarTipado(lista,list))
print(comprobarTipado(numero,int))
print(comprobarTipado(verdadero,bool))
print(comprobarTipado(string,str))
print(comprobarTipado(string,int))