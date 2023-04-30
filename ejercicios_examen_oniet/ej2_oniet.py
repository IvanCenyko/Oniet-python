from time import localtime
import datetime


dia = int(input("ingrese día de nacimiento: "))
mes = int(input("ingrese mes de nacimiento: "))
año = int(input("ingrese año de nacimiento: "))

año_local = localtime()[0]
mes_local = localtime()[1]
dia_local = localtime()[2]

if mes_local > mes:
    cumpleaños = datetime.date(año_local + 1, mes, dia)
else:
    cumpleaños = datetime.date(año_local, mes, dia)
fecha_actual = datetime.date(año_local, mes_local, dia_local)

restante = cumpleaños - fecha_actual
print(f"falta/n {restante.days} día/s")
