denominador = 0

valores = input("ingrese valores: ").split(",")

for valor in valores:
    denominador = denominador + 1/float(valor)

resultado = len(valores) / denominador

print(resultado)
    