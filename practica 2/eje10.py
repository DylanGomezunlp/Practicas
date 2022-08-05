
def promedioNotas (notas1, notas2):
    """toma las listas de notas y calcula el promedio de ambas

    Args:
        notas1 (list): notas del primer archivo
        notas2 (list): notas del segundo archivo

    Returns:
        float: promedio de las notas
    """
    total = 0
    for nota, nota2 in zip (notas1, notas2):
        total += int(nota) + int(nota2)
    return (total/ (len(notas1)+ len(notas2)));

def menorProm (estudiantes, promedio):
    """imprime los estudiantes menores al promedio

    Args:
        estudiantes (dict): estructura generada a partir de los archivos
        promedio (float): promedio de estudiantes
    """
    for estudiante in estudiantes:
        if estudiante['nota'] < promedio:
            print(estudiante)
    return    



with open('nombres1.txt', 'r', encoding = 'utf8') as n:
    nombres = n.read().split()
with open('eval1.txt', 'r', encoding = 'utf8') as n:
    notas1 = n.read().split(',')
with open('eval2.txt', 'r', encoding = 'utf8') as n:
    notas2 = n.read().split(',')

estudiantes = []

for nombre, nota1, nota2 in zip(nombres, notas1, notas2):
    estudiante = {'nombre': nombre, 'nota': int(nota1) + int(nota2)}
    estudiantes.append(estudiante)

promedio = promedioNotas(notas1, notas2)

print(menorProm(estudiantes, promedio))







