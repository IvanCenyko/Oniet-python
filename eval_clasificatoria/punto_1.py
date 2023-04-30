n = int(input("Ingrese un número de Fibonacci: "))
index = 0
num1 = 1
num2 = 1
num3 = 0
if n == 1:
    print("f(1) = 1, o f(2) = 1")
else:
    while not n == num3:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        index = index + 1
    num = index + 2
    print(f"f({num}) = {n}")

