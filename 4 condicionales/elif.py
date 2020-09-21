# print(f"########################## elif ####################")
# dia=int(input("Introduce el dia de la semana "))
# if dia==1:
#     print(f"es lunes")
# elif dia==2:
#     print(f"es martes")
# elif dia==3:
#     print(f"es miercoles")
# elif dia==4:
#     print(f"es jueves")
# elif dia==5:
#     print(f"es viernes")
# elif dia==6:
#     print(f"es jueves")
# elif dia==7:
#     print(f"es domingo")
# else:
#     print(f"opcion incorrecta")
#operadores logicos
#and =y
#or o
#! negacion
#not no
# print(f"########################## elif ####################")
# edad=int(input("Introduce la edad "))
# edad_minima=18
# edad_maxima=65
# if edad>=edad_minima and edad<=edad_maxima:
#     print(f"esta en edad de trabajar")
# else:
#     print("no esta en edad de trabajar")

#mas ejemplos con condicionales
# print(f"########################## condicional con or ####################")
# pais=input("Introduce el pais ")

# if pais=="colombia" or pais=="españa" or pais=="mexico":
#     print(f"{pais} es un pais de habla hispana")
# else:
#     print(f"no es un pais de habla hispana")

# print(f"########################## condicionales con not ####################")
# pais=input("Introduce el pais ")
# if not (pais=="colombia" or pais=="españa" or pais=="mexico"):
#     print(f"{pais} No es un pais de habla hispana")
# else:
#     print(f"{pais} es un pais de habla hispana")

print(f"########################## condicionales con !=####################")
pais=input("Introduce el pais ")
if (pais!="colombia" and pais!="españa" and pais!="mexico"):
    print(f"{pais} No es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")