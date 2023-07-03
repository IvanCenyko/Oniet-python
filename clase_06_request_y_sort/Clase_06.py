import requests
a = int(input())
p = requests.get(f"https://randomuser.me/api?results={a}").json()
lista = []
for i in range (a):
    b = p["results"][i]["name"]["last"]
    lista.append(b)
lista.sort()
print(lista)