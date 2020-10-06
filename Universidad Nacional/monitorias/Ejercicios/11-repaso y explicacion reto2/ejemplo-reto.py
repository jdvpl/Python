from math import ceil
def main():
  total_notas = int(input("Ingrese el número de notas: "))
  #subtotal = 0
  encabezado()
  nota_promediada = promedio(total_notas)
  nota_redondeada = redondea_nota(nota_promediada)
  final(nota_promediada, nota_redondeada)
  print("Gracias por estudiar en la UNAL")

def encabezado():
  print("Sabana notas")
  print("UNAL")

def promedio(total_notas):
  suma = 0
  for _ in range(0,total_notas,1):
    asignatura = input()
    nota = float(input())
    print(f"{asignatura} {nota}")
    suma += nota
  return suma/total_notas

def redondea_nota(nota_promediada): 
  nota_redondeada = round(nota_promediada,1)
  return nota_redondeada

def final(nota_promediada, nota_redondeada):
  print(f"Por el redondeo los decimales eran: {ceil(nota_promediada - nota_redondeada)}")
  print(f"Tu nota final redondeada es {nota_redondeada}")

main()