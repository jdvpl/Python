"""
Extraer nombres de Universidades ColombianasEnunciadoDada una lista de Universidades Colombianas, obtener el nombre del sitioweb.  Se asume que un nombre de universidad est ́a entre los caractereswww.yedu.co.  Por ejemplo dewww.unal.edu.cose obtieneunal

"""
def process(uni):
    return uni.split(".")[1]
    
def main():
    n = int(input("N ́umero de Universidades: "))
    for i in range(n):
        uni = input("Universidad " + str(i+1) + ": ")
        print(process(uni))
main()