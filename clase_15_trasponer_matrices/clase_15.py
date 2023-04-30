import math

lado = float(input('Ingrese longitud de lado en cm: '))

altura = math.sqrt(lado**2 - (lado/2)**2)

ladom = altura / 100

print (f'La altura es {ladom} m')

