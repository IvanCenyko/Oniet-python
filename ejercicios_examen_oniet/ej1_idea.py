valores = input("Ingrese valores: ")

lista_valores = list(valores)
lista_index = []
valores_pasados = []

for valor in lista_valores:
    if not valor == ",":
        lista_index.append(valor)
    else:
        num = "".join(lista_index)
        valores_pasados.append(num)
        lista_index = []
    
num = "".join(lista_index)
valores_pasados.append(num)

print(valores_pasados)
