"""
La prueba de ADNEnunciadoEn la  ́ultima edici ́on de la revista cient ́ıfica “ADN al d ́ıa” se indica que laspruebas de relaci ́on entre individuos a partir de c ́odigo gen ́etico se definede la siguiente manera:  Si las dos cadenas se diferencian en a lo m ́aspletras, existe una relaci ́on de padre-hijo, si se diferencian en a lo m ́asf>pletras, existe una relaci ́on de formar parte de la misma familia.  De otramanera no existe relaci ́on.  El laboratorioTein Cul Pan, le pide desarrollarun programa que a partir de dos cadenas de ADN del mismo tama ̃no,determine si existe una relaci ́on padre-hijo, o de la misma familia oninguna, siguiendo las reglas definidas por la revista cient ́ıfica “ADN ald ́ıa

"""
def dif(a, b):
    cuenta = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            cuenta = cuenta + 1
    return cuenta
def relacion(a, b, p, f):
    d = dif(a, b)
    if d <= p:
        return 'Padre-Hijo'
    elif d <= f:
        return 'Familia'
    else:
        return 'Ninguna'

ind1 = input('¿Cadena ADN individuo 1?: ')
ind2 = input('¿Cadena ADN individuo 2?: ')
p = int(input('Diferencia maxima para ser Padre-Hijo?: '))
f = int(input('Diferencia maxima para ser Familia?: '))
print("Relaci ́on", relacion(ind1, ind2, p, f))