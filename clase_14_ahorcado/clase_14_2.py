palabra = 'messi'
vidas = 5
palabra_list = list(palabra)
palabra_progreso = list(palabra)
palabra_len = len(palabra_list)

progreso = []
letras_usadas = []
lineado = '------------------------------------------------'

for _ in range(palabra_len):
    progreso.append('*')

while not vidas == 0 and not ''.join(progreso) == palabra:
    letra = input('Ingrese letra: ')

    if letra in letras_usadas:
        print('Ya la usaste')
        print(lineado)

    elif not letra in letras_usadas:
        index = 0
        letras_usadas.append(letra)


        if not letra in palabra_list:
            vidas = vidas - 1
            print(''.join(progreso))
            print ('Letra equivocada.')
            print(f'Letras usadas: {letras_usadas}')
            print (f'Te quedan {vidas} vidas')
            print(lineado)

        while letra in palabra_progreso:
            for l in palabra_list:
                if l == letra:
                    palabra_progreso.remove(letra)
                    progreso[index] = l
                index = index + 1

            print(''.join(progreso))
            print(f'Letras usadas: {letras_usadas}')
            print(lineado)



if ''.join(progreso) == palabra:
    print ('Ganaste!')
elif vidas == 0:
    print('Perdiste!')        
        


            

