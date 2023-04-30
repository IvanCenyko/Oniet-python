palabra = 'messi'
vidas = 5
palabra_list = list(palabra)
palabra_largo = len(palabra_list)
resultado = []
letras = []
erroneas = []
for _ in range(palabra_largo):
    resultado.append('*')

while vidas != 0:
    letra = input('ingrese letra: ')
    if letra in letras:
        print('ya la usaste boludito')
    



    if not letra in letras:


        if letra in palabra_list:
            for l in palabra_list:

                if letra == l:
                    for i in range(palabra_largo):
                        if palabra_list[i] == letra:
                            posicion = i
                    resultado[posicion] = l
        print(''.join(resultado))

        if not letra in palabra_list:
            vidas -=1
            erroneas.append(letra)
            print(f'perdiste una vida, te quedan {vidas}')
            print(''.join(resultado))
            print('letras incorrectas',erroneas)



    print("_______________________________________")
    letras.append(letra)
    



if vidas == 0:
    print('perdiste jaja xd')





