palabra1 = input("ingrese palabra:")
palabra2 = input("ingrese palabra:")

palabra1 = palabra1.lower()
palabra2 = palabra2.lower()
palabra1.replace(",","")
palabra2.replace(",","")
palabra1.replace(" ","")
palabra2.replace(" ","")

palabra1_arreglo = list(palabra1)
palabra2_arreglo = list(palabra2)

palabra1_arreglo.sort()
palabra2_arreglo.sort()

palabra1_ordenada = "".join(palabra1_arreglo)
palabra2_ordenada = "".join(palabra2_arreglo)

if palabra1_ordenada == palabra2_ordenada:
    print ("Hay anagrama")
else:
    print("no hay anagrama")