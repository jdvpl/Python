# importar modulo de sqlite
import sqlite3

# conexion
ruta='./18 sqlite/'
conexion=sqlite3.connect(ruta+'Pruebas.db')
# crear cursor
cursor=conexion.cursor()
# crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo varchar(255), "+
"descripcion text, "+
"precio int(11)"+
")")
# GUARDAR CAMBIOS
conexion.commit()
# insertar datos
nombre=input("Ingrese el nombre del producto: ")
des=input(f"Ingrese una descripcion de {nombre}: ")
pre=int(input(f"Ingrese el precion de {nombre}: "))
cursor.execute(f"INSERT INTO productos VALUES(null,'{nombre}','{des}',{pre})")

conexion.commit()

# listar datos
cursor.execute("SELECT * FROM productos")
productos=cursor.fetchall()

for producto in productos:
    print(f"Nombre: {producto[1]}, Descripcion: {producto[2]}, Precio: {producto[3]}")


# cerrar conexion
conexion.close()