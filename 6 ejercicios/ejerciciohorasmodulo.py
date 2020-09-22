# hora=int(input("Ingresa la Hora inicial "))
# final=int(input("ingresa dentro de cuantas horas quiere que suene la alarma "))
# hora_fina=final%24
# print(hora+hora_fina)

print("############# Hora Inicial ##################\n".center(60))
while True:
    try:
        hora,minutos,segundos=(input("Ingrese la Hora inicial, hh:mm:ss ejemplo 22:15:25 \n").split(":"))
        break
    except ValueError:
        print("El valor es incorrecto, debes ingresar tres numeros seguidos por : ejemplo 10:15:20")

print("#### Alarma #####".center(50))
while True:
    try:
        horaa,minutosa,segundosa=(input("Ingrese hora en cuanto quiere que suene hh:mm:ss, ejemplo 22:15:25 \n").split(":"))
        break
    except ValueError:
        print("El valor es incorrecto, debes ingresar tres numeros seguidos por : ejemplo 10:15:20")
        
        # formateando la hora incial
hora=int(hora)
minutos=int(minutos)
segundos=int(segundos)

segundostotalesiniciales=segundos%60
minutos=minutos+(segundos//60)
totalminutosiniciales=minutos%60
hora=hora+(minutos//60)
totalhorainicial=hora%24

print(f"\n\n########## Hola Inicial #####")
print(f"{totalhorainicial}:{totalminutosiniciales}:{segundostotalesiniciales}")

print("\n")
horaa=int(horaa)
minutosa=int(minutosa)
segundosa=int(segundosa)

segundostotalesfinales=segundosa%60
minutosa=minutosa+(segundosa//60)
totalminutosfinal=minutosa%60
horaa=horaa+(minutosa//60)
totalhorafinal=horaa%24
dia=horaa//24

horafina=totalhorainicial+totalhorafinal
minutofinal=totalminutosiniciales+totalminutosfinal
segundofinal=segundostotalesiniciales+segundostotalesfinales

segundosfinales=segundofinal%60
minutofinal=minutofinal+(segundofinal//60)
minutosfinales=minutofinal%60
horafina=horafina+(minutofinal//60)
horafinal=horafina%24
dia=dia+(horafina//24)



print(f"Hora de alarma {dia}d:{totalhorafinal}:{totalminutosfinal}:{segundostotalesfinales}")
print(f"Sonara a el {dia} dia, a las {horafinal}:{minutosfinales}:{segundosfinales}")










