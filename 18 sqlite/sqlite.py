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

# cerrar conexion
conexion.close()