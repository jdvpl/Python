"""
el programa tiene que pedir la nota de n estudiantes y sacar en pantalla cuantos apreobaron y cuantos
reprobaron

"""
cantidad=int(input("Introduzca la cantidad de estudiantes: "))
aprobados=0
reprobados=0
contador=1
while contador<=cantidad:
    nota=float(input(f"que nota quieres ponerle al alumno {contador} "))
    if nota>=5:
        aprobados+=1
    else:
        reprobados+=1

    contador+=1
print(f"La cantidad de alumnos rerobados son {reprobados} y los que aprobaron son: {aprobados}")