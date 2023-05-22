# √
# list = [7, 6, 4, 5, 7, 'hello']
# var = list[0] #guardo en var lo que haya en el index 0
# list.append(1) #añado el numero 1 a la ultima posición
# list.remove(2) #quito el numero 2 de la lista
# list.pop(0) #quito el index 0 de la lista
# print(list)

import math

list = [] #lista vacía
num = 0
con = 0


while True:
    num2 = float(input("Ingrese un numero: ")) #input numero 2
    if con == 1:
        num1 = num
    elif not con == 1:
        num1 = float(input("Ingrese un numero: ")) #input numero 1
    op = input("Ingresa la operacion: ") #tipo de operacion

    if op == "+":
        num = num1+num2
    elif op == "-":
        num = num1-num2
    elif op == "/":
        num = num1/num2
    elif op == "*":
        num = num1*num2
    elif op == "^":
        num = math.pow(num1, num2)
    elif op == "√":
        num = math.pow(num1, 1/num2)
    print(num)
    con = int(input("desea seguir operando? so = 1 no = 2"))
