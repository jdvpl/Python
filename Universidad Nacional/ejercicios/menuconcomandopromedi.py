"""
Leer informaci ́on de estudiantes y calcular el promedio de notasEnunciadoSe tienen que procesar algunos comandos para realizar el procesamiento denotas de una Universidad.  Se tiene una lista de estudiantesComando 1:  Agregar estudiante y nota1&nombre_estudiante&notaComando 2:  Calcular promedio de los estudiantes en un momento dadoComando 3:  Ordenar estudiantes agregados por nombreComando 4:  Consultar la nota de un estudiante4&nombre_estudianteComando 5:  Visualizar lista de estudiantesComando 6:  Salir(Pensemos por 5 minutos en la soluci ́on)G ́omez, Rodr ́ıguez & Cubides   (UN)Repaso 230 / 38
Leer informaci ́on de estudiantes y calcular el promedio de notasAn ́alisisPara poder resolver el problema se puede dividir dicho problema enproblemas m ́as peque ̃nos que son:Definir la lista de estudiantes.Agregar un estudiante dada la informaci ́onCalcular el promedio de notas de los estudiantes en un momento dadoOrdenar estudiantes agregados por nombreConsultar la nota de un estudianteVisualizar listaProcesar los comandosMostrar men ́u
"""

def agregar_estudiante(estudiantes, est):
    estudiantes.append(est)

def promedio(estudiantes):
    prom = 0
    for estudiante in estudiantes:
        prom += float(estudiante[1])
        print("El promedio de los estudiantes es: ")
        print(prom/len(estudiantes))

def ordenar(estudiantes):
    estudiantes.sort()

def consultar(estudiantes, nombre):
    encontrado = False
    for estudiante in estudiantes:
        if estudiante[0] == nombre:
            encontrado = True
            print(estudiante[1])
    if not encontrado:
        print("Estudiante no encontrado")

def visualizar(estudiantes):
    print("Lista de estudiantes".center(30, "#"))
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    for e in estudiantes:
        print("Nombre: " + e[0] + ", nota: " + str(e[1]))

def mostrar_menu():
    print("Seleccione una opci ́on: ")
    print("Comando 1: Agregar estudiante y nota"" ’1&nombre_estudiante&nota’")
    print("Comando 2: Calcular promedio de los"" estudiantes en un momento dado")
    print("Comando 3: Ordenar estudiantes agregados por nombre")
    print("Comando 4: Consultar la nota de un estudiante"" ’4&nombre_estudiante’")
    print("Comando 5: Visualizar")
    print("Comando 6: Salir")

def procesar_comandos():
    bandera = True
    estudiantes = []
    comando = [0]
    while bandera or comando[0] != "6":
        bandera = False
        mostrar_menu()
        comando = input().split("&")
        print(comando[0])
        if comando[0] == "1":
            agregar_estudiante(estudiantes,(comando[1], float(comando[2])))
        elif comando[0] == "2":
            promedio(estudiantes)
        elif comando[0] == "3":
            ordenar(estudiantes)
        elif comando[0] == "4":
            consultar(estudiantes, comando[1])
        elif comando[0] == "5":
            visualizar(estudiantes)

procesar_comandos()