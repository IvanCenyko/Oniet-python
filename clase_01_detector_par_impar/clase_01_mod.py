while 1:   
    valor = int(input ('ingrese un numero: '))

    if valor == 0:
        print('El numero es cero')

    elif valor % 2 == 0:
        print(f'El numero {valor} es par')
    else:
        print(f'El numero {valor} es impar')