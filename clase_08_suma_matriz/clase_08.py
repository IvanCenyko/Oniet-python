m1 = [
    [1, 5, 6],
    [0, -2, 4]
]

m2 = [
    [8, -5, 1],
    [0, 0, 1]
]

def sumaMatrices(m1, m2):

    aux = []
    filas = len(m1)
    for i in range(filas):

        auxFila = []
        fila = m1[i]
        columnas = len(fila)
        for j in range(columnas):

            auxFila.append(fila[j] + m2[i][j])

        aux.append(auxFila)

    return aux

print(sumaMatrices(m1, m2))
print(m1)