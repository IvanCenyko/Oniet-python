velocidad = 1
index = 0
velocidades = []
while velocidad != 0:
    index = index +1
    velocidad = float(input(f'Ingrese velocidad del avion {index}: '))
    velocidades.append(velocidad)

velocidades.remove(velocidades[-1])

vel_sonido = 1234.8

for i in range(len(velocidades)):
    resultado = velocidades[i] / vel_sonido
    if resultado > 1:
        print('Supersonico')
    else:
        print('No supersonico')