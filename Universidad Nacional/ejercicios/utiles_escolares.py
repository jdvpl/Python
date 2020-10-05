"""
Unos padres de familia desesperados por determinar el dinero 
que debenpedir prestado para pagar los  ́utiles escolares de su hijo,
 le han pedidocrear un programa de computador que a partir de una lista
  de los preciosde cada  ́util escolar y de la cantidad de cada 
 ́util escolar en la lista,determine el precio total de la lista.

"""
def costo_total(precio, cantidad):
    costo = 0
    for i in range(0,len(precio)):
        costo += precio[i] * cantidad[i]
    return costo

precio = []
cantidad = []
while input('¿Ingresar otro  ́util?: ').upper() == 'S':
    precio.append(float(input('¿Precio  ́util?: ')))
    cantidad.append(float(input('¿Cantidad?: ')))
print("La lista cuesta", costo_total(precio, cantidad))