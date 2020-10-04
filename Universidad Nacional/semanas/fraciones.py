"""
Utilizando funciones recursivas, elabore un programa que simplifique una fracción escrita de la forma a/b.
"""
from fractions import Fraction
        
amplificado=input("ingrese numero '/':")
numerador,denominador=amplificado.split("/")
numerador=int(numerador)
denominador=int(denominador)

print(Fraction(numerador/denominador))


