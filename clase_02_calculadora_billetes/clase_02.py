billetes = [100, 50, 20, 10, 5, 1]

monto = int(input('Ingrese monto: '))

# 346

index = 0   # elementos
while index < len(billetes): #escribo los elementos
    b = monto // billetes[index]
    monto = monto - b * billetes[index]
    if b != 0:
        print(f'cantidad de {billetes[index]}: {b}')


'''

for billete in billetes:
    b = monto // billete
    monto = monto - b * billete
    if b != 0:
        print(f'Cantidad  de {billete}: {b}')
        
'''