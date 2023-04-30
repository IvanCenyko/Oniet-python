numeros = []
for _ in range(5):
    numero = float(input('ingrese numero: '))
    numeros.append(numero)
    
maximo = max(numeros)
minimo = min(numeros)
min_index = numeros.index(minimo)
max_index = numeros.index(maximo)

print(f'el maximo es {maximo} en {max_index + 1} y el minimo es {minimo} en {min_index + 1}')
prom = 0
for num in numeros:
    prom = prom + num
prom = prom/len(numeros)
print(f'El promedio es: {prom}')
numeros.sort()
print(numeros)
