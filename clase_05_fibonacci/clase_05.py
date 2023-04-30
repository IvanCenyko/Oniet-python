def fibonacci(n):

  # La serie arranca en el par 1 1
  num1 = 1
  num2 = 1
  # Repito el algoritmo de abajo n veces
  for _ in range(n):
    # Obtengo el siguiente elemento de la serie
    num3 = num1 + num2
    # Descarto el primer elemento que ya no sirve
    num1 = num2
    # Como el segundo elemento fue copiado, puedo pisarlo con la suma
    num2 = num3
    # Repito

  return num3

n = int(input("Ingrese el elemento n de la serie que desea obtener: "))
print(f"El elemento es {fibonacci(n)}")