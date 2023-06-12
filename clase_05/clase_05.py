# lista vacia
list = []

# repito el input cuatro veces y los guardo en  la lista
for _ in range(4):
    num = int(input("Ingrese valor: "))
    list.append(num)

# ordeno la lista de menor a mayor
list.sort()

# saco el promedio de los numeros de la lista
suma = 0
for i in list:
    suma += i
promedio = suma / len(list)

# printeo la lista, el valor maximo, el valor minimo y el promedio
print(max(list))
print(min(list))
print(promedio)
print(list)
