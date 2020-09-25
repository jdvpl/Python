"""
programa que comprueba si una variable esta vacia y si esta, la rellna con
texto en minusculas y mostrarlo en mayuscula
"""
texto=""

if len(texto.strip())<=0:
    # mostrar el texto
    texto="hola soy un texto en minusculas "
    print(texto.upper())
else:
    print(f"La va tiene contenido {texto}")