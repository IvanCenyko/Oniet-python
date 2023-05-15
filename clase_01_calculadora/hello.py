# var = int(input('Ingrese numero: '))

# + - * /

# if var == 2:
#     print('el numero es 2')
# elif var == 3:
#     print('el numero es 3')
# else:
#     print('el numero no es ni dos ni tres')

num1 = float(input("Ingrese un numero: ")) #input numero 1
num2 = float(input("Ingrese un numero: ")) #input numero 2
op = input("Ingresa la operacion: ") #tipo de operacion

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Hubo un error al ejecutar la calculadora")