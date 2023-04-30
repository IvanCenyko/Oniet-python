word = input("Ingrese palabra: ")
word = word.replace(",", "")
word = word.replace(" ", "")
word = word.lower()
if str(word) == "".join(reversed(word)) :
    print("Palindrome")
else:
    print("Not Palindrome")