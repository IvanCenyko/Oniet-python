import csv

archivo = open(r"./archivo.csv")

with open(r"./archivo.csv", 'r') as file:
  archivo = csv.reader(file)
  for row in archivo:
    print(row)


[
  ['#', 'equipo', 'puntos'],
  ['1', 'River', '80'],
  ['2', 'Talleres', '78']
]