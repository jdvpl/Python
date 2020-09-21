"""
El banco unaleño requiere su ayuda para la implementación de cajeros electrónicos en ciudad Gótica. 
Gótica tiene billetes de $10.000, $20.000, $50.000 y $100.000.

El banco desea emplear la menor cantidad de billetes posibles cuando un ciudadano realiza un retiro.
 El banco en otro desarrollo de software ya se aseguró de que la cantidad de dinero a retirar sea múltiplo de 10000.

Entrada

La entrada es un valor a retirar. Se garantiza que el valor a retirar es múltiplo de 10.000

Salida

El número de billetes a repartir de cada denominación en el formato mostrado en las ejecuciones de ejemplo:
entrada                         Salida
	
560000                          5 x $100000

                                1 x $50000

                                0 x 20000

                                1 x $10000
"""
plata=int(input("Ingrese la plata a retirar: "))

cien=plata//100000
plata=plata-cien*100000

cincuen=plata//50000
plata=plata-cincuen*50000

veinte=plata//20000
plata=plata-veinte*20000

diez=plata//10000
print(f"{cien} x $100000")
print(f"{cincuen} x $50000")
print(f"{veinte} x $20000")
print(f"{diez} x $10000")



