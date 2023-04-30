import requests


class PersRandom(object):
    def __init__(self):
        self.pais = 0
        self.edad = 0

    def search(self):
        response = requests.get('https://randomuser.me/api?results=1').json()
        self.edad = response['results'][0]['dob']['age']
        self.pais = response['results'][0]['location']['country']
    def returnEdad(self):
        return self.edad
    def returnPais(self):
        return self.pais

p1 = PersRandom()
p1.search()
print('La edad es:', p1.returnEdad())

