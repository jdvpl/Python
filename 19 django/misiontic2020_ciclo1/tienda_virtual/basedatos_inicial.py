from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db_tienda_virtual = client.tiendaVirtual

lista_inicial = [
    {'nombre': "Camistea React", 'costo': 107500},
    {'nombre': "Camistea Angular", 'costo': 107500},    
]
ids_ = db_tienda_virtual.productos.insert_many(lista_inicial)
print(ids_)