# lo mas recomendable en una funcion es que devuelva un dato osea con retunr
# funciones al inicio
# https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/19049246#notes
def main(nombre):
    return f"\nInsecto {nombre}"
def main2(apellidos):
    return f"kisama {apellidos}"

nombre="Juan Daniel "
apellidos="suarez"

print("\nhola mundo")
print(f"bienvenidos {nombre}")
# seimpre es recomendable que las variables ya esten definidas
print(main(nombre))
print(main2(apellidos))