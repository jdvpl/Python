billete_100k = 100000
billete_50k = 50000
billete_20k = 20000
billete_10k = 10000

dinero_a_retirar = int(input("Digite el valor a retirar. Recuerde que debe ser multiplo de $10.000: "))
billetes_100k = dinero_a_retirar // billete_100k  #5
residuo = dinero_a_retirar % billete_100k #60000

billetes_50k = residuo // billete_50k #1
residuo = residuo % billete_50k #10000

billetes_20k = residuo // billete_20k #0
residuo = residuo % billete_20k #10000

billetes_10k  = residuo // billete_10k #1

#print(str(billetes_100k) + " x $100000")
#print(str(billetes_100k), "x $100000")
print(billetes_100k, "x $100000")
print(billetes_50k, "x $50000")
print(billetes_20k, "x $20000")
print(billetes_10k, "x $10000")
#print('{} x $100000  Billetes de 50=$ {} Billetes de 20=$ {} Billetes de 10=$ {}'.format(billetes_100k,billetes_50k,billetes_20k, billetes_10k))