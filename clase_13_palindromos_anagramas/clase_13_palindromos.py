word = input('ingrese palabra o frase: ')

fase0 = word.lower()
fase1=fase0.replace(",","")
fase2=fase1.replace(" ","")

if str(fase2) == str(fase2)[::-1] :
    print("Es palindromo")
else:
    print("No es palindromo")