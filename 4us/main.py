from machine import Pin
import time

tiempo = 0
end = 0
start = 0

p1 = Pin(12, Pin.IN)
p2 = Pin(14, Pin.IN)
rele = Pin(2, Pin.OUT)

rele.off()
        
while tiempo == 0: #calcula el tiempo de una vuelta
    while start == 0:
        if p2.value():
            start = time.ticks_ms()
    if p1.value():
        end = time.ticks_ms()
    if not end == 0 and not start == 0:
        tiempo = (end - start) * 2
    base = time.ticks_ms()

print(tiempo) #tiempo de una vuelta
rele.on()
while 1: #printea el porcentaje de vuelta
    start = time.ticks_ms() - base
    porcentaje = ((start / tiempo) - int (start / tiempo))* 100
    if porcentaje == 75:
        rele.off()
        break

