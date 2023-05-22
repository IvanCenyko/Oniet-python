# √
# list = [7, 6, 4, 5, 7, 'hello']
# var = list[0] #guardo en var lo que haya en el index 0
# list.append(1) #añado el numero 1 a la ultima posición
# list.remove(2) #quito el numero 2 de la lista
# list.pop(0) #quito el index 0 de la lista
# print(list)
import math

resultados = [] #lista vacía


while True:
    num1 = input("Ingrese un numero: ") #input numero 1
    num2 = input("Ingrese un numero: ") #input numero 2
    op = input("Ingresa la operacion: ") #tipo de operacion

    #si yo ingreso en el primer input 'ans'
    if num1 == 'ans':
        num1 = resultados[-1]
    else:
        num1 = float(num1)

    #si yo ingreso en el segundo input 'ans'
    if num2 == 'ans':
        num2 = resultados[-1]
    else:
        num2 = float(num2)

    #calculo
    if op == "+":
        res = num1+num2
    elif op == "-":
        res = num1-num2
    elif op == "/":
        res = num1/num2
    elif op == "*":
        res = num1*num2
    elif op == "^":
        res = math.pow(num1, num2)
    elif op == "√":
        res = math.pow(num1, 1/num2)
    
    #guardo el resultado en el historial y printeo
    resultados.append(res)
    print(res)
