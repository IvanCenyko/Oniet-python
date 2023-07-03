from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template
import datetime

datas = []

def datos(request):
    global datas
    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        curso = request.POST["curso"]
        fecha_hora = request.POST["fecha_hora"]

        data = [nombre, apellido, curso, fecha_hora]
        datas.append(data)
        return HttpResponse("Done!")
    else:
        return render(request, "template.html", context={"datas":datas})