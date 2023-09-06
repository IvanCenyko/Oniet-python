mano = [1,4,7,8]

nueva = 3

def anadir(carta_nueva, cartas):
    index = 0

    for carta in cartas:
        if carta < carta_nueva:
            index +=1
        else:
            cartas.insert(index, carta_nueva)
            break

anadir(nueva, mano)
print(mano)