fib1 = 0 # fib 1
fib2 = 1 # fib 2
fibr = 1 # resultado de fib(1), seria mi caso inicial

n = int(input('Ingrese digito de Fibonacci: '))

# separo el caso del 0
if n == 0:
    print('Fibonacci(0) = 0')

#para todos los otros casos
else:
    for _ in range(n-1): # n-1 para que fib(1) no ejecute el for y devuelva fib(1) = 1
        fibr = fib1 + fib2

        fib1 = fib2
        fib2 = fibr
    
    print(f'Fibonacci({n}) = {fibr}')