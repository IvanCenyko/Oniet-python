import math
x1 = float(input("Ingrese x1(m): "))
y1 = float(input("Ingrese y1(m): "))
x2 = float(input("Ingrese x2(m): "))
y2 = float(input("Ingrese y2(m): "))

distancia_total = math.sqrt(abs(x2 - x1)**2 + abs(y2-y1)**2)
dist_cm = distancia_total * 100
print("La distancia entre los puntos es de: {:.2f}".format(dist_cm))