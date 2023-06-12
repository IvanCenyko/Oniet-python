# formato de un diccionario
dict = {
    "cosa1": 4,
    "cosa2": 3
}


# importo libreria para hacer requests web
import requests


# guardo en response la informacion web de la pagina "randomuser"
response = requests.get('https://randomuser.me/api?results=1')

#convierto la respuesta a json para que se lea como un diccionario
rjson = response.json()

#de lo que me devolvio la pagina, busco el primer nombre y el apellido del usuario aleatorio
print(rjson['results'][0]['name']['first'])
print(rjson['results'][0]['name']['last'])