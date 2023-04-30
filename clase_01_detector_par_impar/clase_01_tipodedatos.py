while 1:   
    valor = int(input ('ingrese un numero: '))
    dividido = (valor/2)
    resultado = dividido - int (dividido)

    if resultado == 0:
        print(f'El numero {valor} es par')

    else:
        print(f'El numero {valor} es impar')



