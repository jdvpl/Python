def main():
    contagios_a = int(input("Ingrese los contagios en el país A en el día 1: "))
    contagios_b = int(input("Ingrese los contagios en el país B en el día 1: "))
    dia = 1
#n (1 <=contagios_a <= 10^8)
#  (1 <= contagios_b <= contagios_a).
    if(1 <=contagios_a <= 10**8 and 1 <= contagios_b <= contagios_a):
        while (contagios_b < contagios_a):
            contagios_a = contagios_a*1.02 #solucion alternativa: contagios_a + (contagios_a*0.02)
            contagios_b = contagios_b*1.03
            dia +=1
        print(dia)
    else:
        print("Error en los datos ingresados")
main()