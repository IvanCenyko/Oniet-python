import requests, json, datetime

data = {
    "nombre": "nashe",
    "apellido": "nashe",
    "curso": "nashe",
    "fecha_hora": datetime.datetime.now()
}


requests.post("http://127.0.0.1:8000/datos", data=data)