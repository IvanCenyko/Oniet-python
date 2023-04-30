alumnos = 0
reprobados = 0
notas_rep = []
menor = 0

while alumnos < 10 or alumnos > 100:
    alumnos = int(input('Ingrese cantidad de alumnos: '))
    if alumnos < 10 or alumnos > 100:
        print('Ingrese una cantidad valida')

prom_total = float(input('Ingrese el promedio total de nota de alumnos: '))

while reprobados < 2 or reprobados > 10:
    reprobados = int(input('Ingrese cantidad de reprobados: '))
    if reprobados < 2 or reprobados > 10:
        print('Ingrese una cantidad valida')

for i in range(reprobados):
    nota = float(input(f'ingrese nota del reprobado {i+1}: '))
    notas_rep.append(nota)

while menor < 4:
    menor = float(input('Ingrese la nota menor de los alumnos aprobados: '))
    if menor < 4:
        print('Ingrese una cantidad valida')

p_reprobados = 0
for i in notas_rep:
    p_reprobados = i + p_reprobados

p_total= alumnos * prom_total

prom_aprobados = (p_total - p_reprobados) / (alumnos - reprobados)

print(f'El promedio de los aprobados es {prom_aprobados}')
