from machine import Pin, Timer, PWM
import utime

def duty_grados(grados):
    return int(duty_us(500 + grados * 2000 / 180))
def duty_us(us):
    t = 1 / 50
    return int(us / 1e6 * (1 << 16) / t)

p16 = Pin(16, Pin.IN)
p14 = Pin(14, Pin.IN)

servo = PWM(Pin(15))
servo.freq(50)

while 1:
    if not p16.value():
        servo.duty_u16(duty_grados(48)) #48 abierto-112 cerrado
        utime.sleep(2)

