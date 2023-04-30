import requests

response = requests.get('https://randomuser.me/api?results=1')
rjson = response.json()
edad = rjson['results'][0]['dob']['age']
pais = rjson['results'][0]['location']['country']
print(f'su edad es de {edad} años y su pais es {pais}')
