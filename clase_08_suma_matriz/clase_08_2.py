m1 = [
    [1, 5, 6],
    [0, -2, 4]
]

m2 = [
    [8, -5, 1],
    [0, 0, 1]
]

matriz_final = []
fila_aux = []
filas = len(m1)
columnas = len(m1[0])

for fila in range(filas):
    for columna in range(columnas):
        suma = m1[fila][columna] + m2[fila][columna]
        fila_aux.append(suma)
    matriz_final.append(fila_aux)
    fila_aux = []

print(matriz_final)

