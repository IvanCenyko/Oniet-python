import math
x1 = int(input("Ingrese x1: "))
y1 = int(input("Ingrese y1: "))
x2 = int(input("Ingrese x2: "))
y2 = int(input("Ingrese y2: "))

dist_1 = math.sqrt(x1*x1 + y1*y1)
dist_2 = math.sqrt(x2*x2 + y2*y2)

if dist_1 < dist_2:
    print("El punto 1 está más cerca del origen.")
elif dist_2 < dist_1:
    print("El punto 2 está más cerca del origen.")

distancia_total = math.sqrt(abs(x2 - x1)**2 + abs(y2-y1)**2)
print(f"La distancia entre los puntos es de: {distancia_total}")