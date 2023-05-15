from machine import Pin
from time import sleep

IN1 = Pin(15,Pin.OUT)
IN2 = Pin(14,Pin.OUT)
IN3 = Pin(13,Pin.OUT)
IN4 = Pin(12,Pin.OUT)
p16 = Pin(16, Pin.OUT)



def paso_a_paso(angulo):
    pins = [IN1, IN2, IN3, IN4]
    sequence = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

    index = 0
    valor = angulo * 50 / 360

    for _ in range(valor):
        for step in sequence:
            for i in range(len(pins)):
                pins[i].value(step[i])
                sleep(0.002)
            index += 1
            print(index) 




paso_a_paso(240)



'''
for _ in range(degrees(240)):
    for step in sequence:
        for i in range(len(pins)):
            pins[i].value(step[i])
            sleep(0.002)
        index += 1
        print(index)

while not p16.value():
    for step in sequence:
        for i in range(len(pins)):
            pins[i].value(step[i])
            sleep(0.002)
        index += 1
        print(index)
'''