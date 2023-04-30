import numpy as np
tipo_matriz = 0
index = 0
index2 = 0
matriz_parcial = []
matriz1 = []
matriz2 = []

while tipo_matriz != '3x3' and tipo_matriz != '4x4':
    tipo_matriz = input('Ingrese tipo de matriz: ')
    if tipo_matriz != '3x3' and tipo_matriz != '4x4':
        print('Ingrese un tipo valido')

if tipo_matriz == '3x3':
    for _ in range (3):
        index2 = index2 + 1
        for _ in range(3):
            index = index + 1
            valor = int(input(f'Ingrese el valor a{index2}{index}: '))
            matriz_parcial.append(valor)
        index = 0
        matriz1.append(matriz_parcial)
        matriz_parcial = []
    index = 0
    index2 = 0
    for _ in range (3):
        index2 = index2 + 1
        for _ in range(3):
            index = index + 1
            valor = int(input(f'Ingrese el valor b{index2}{index}: '))
            matriz_parcial.append(valor)
        index = 0
        matriz2.append(matriz_parcial)
        matriz_parcial = []

elif tipo_matriz == '4x4':
    for _ in range (4):
        index2 = index2 + 1
        for _ in range(4):
            index = index + 1
            valor = int(input(f'Ingrese el valor a{index2}{index}: '))
            matriz_parcial.append(valor)
        index = 0
        matriz1.append(matriz_parcial)
        matriz_parcial = []
    index = 0
    index2 = 0
    for _ in range (4):
        index2 = index2 + 1
        for _ in range(4):
            index = index + 1
            valor = int(input(f'Ingrese el valor b{index2}{index}: '))
            matriz_parcial.append(valor)
        index = 0
        matriz2.append(matriz_parcial)
        matriz_parcial = []


suma = np.array(matriz1) + np.array(matriz2)

print (suma)