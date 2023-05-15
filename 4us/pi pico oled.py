import random
from machine import Pin, SoftSPI
import st7789py as st7789
from time import sleep
import vga2_bold_16x32 as font

#up = Pin(2,Pin.IN)
#dw = Pin(3,Pin.IN)
#ok = Pin(4,Pin.IN)
#ind = Pin(5,Pin.IN)
#sensamp = ADC(0)

spi = SoftSPI(
    baudrate=20000000,
    polarity=1,
    phase=0,
    sck=Pin(2),
    mosi=Pin(3),
    miso=Pin(8))

display = st7789.ST7789(
    spi,
    240,
    240,
    reset=Pin(0, Pin.OUT),
    cs=Pin(16, Pin.OUT),
    dc=Pin(1, Pin.OUT),
    rotation=0)


display.fill(0)
values = [10, 15, 20, 5, 100, 50]

for i in values:
    display.rect(40, 40, 70, 70, 0)
    display.text(font, str(i), 40, 40)
    sleep(1)
'''
def start_up():
    display.fill(0)
    display.text(font,"4us",20,30)
    display.text(font,"Proyect",20,60)
    display.text(font,"Running - v1",20,150)


def detect_metales():
    display.fill(0)
    while True:
        display.text(font,"Metales",50,20)
        if up.value() == False:
            return
        if ind.value():
            display.text(font,"no",50,60)
        else:
            display.text(font,"si",50,60)

def sens_amp():
    display.fill(0)
    while True:
        display.text(font,"Amplitud",50,20)
        """
        if up.value() == False:
            return
        """
        amp = str(sensamp.read()/10)
        display.text(font,amp,50,60)


def cayo_algo():
    amp = int(sensamp.read()/10)
    normal = amp
    calculado = normal*1.0050
    cant = 0
    display.fill(0)
    while True:
        amp = int(sensamp.read()/10)
        if amp >= calculado:
            display.text(font,"cayo algo",50,20)
            cant = cant+1
        else:
            amp = str(amp)
            display.text(font,"nada",50,20)
            display.text(font,amp,50,60)
        if cant > 0:
            strant = str(cant)
            display.text(font, "cayeron cosas",20,20)
            display.text(font, strant,200,20)
        if up.value() == False:
            return

def cayo_metal():
    amp = int(sensamp.read()/10)
    normal = amp
    calculado = normal*1.0050
    cant = 0
    display.fill(0)
    while True:
        amp = int(sensamp.read()/10)
        if amp >= calculado and ind.value() == False:
            display.text(font,"cayo algo",50,20)
            cant = cant+1
        else:
            amp = str(amp)
            display.text(font,"nada",50,20)
            display.text(font,amp,50,60)
        if cant > 0:
            strant = str(cant)
            display.text(font,"cayeron metales",0,40)
            display.text(strant,200,40)
        if up.value() == False:
            return

def comunicar():
    # esta es la funcion sobre la que hay que implementar la com.
    display.fill(0)
    display.text(font,"Enviando...",50,20)
    sleep(2)
    return


def main_menu():
    cont = 0
    display.fill(0)
    while True:
        if up.value() == True:
            cont = cont+10
        if dw.value() == True:
            cont = cont-10
        if ok.value() == False:
            if cont == 0:
                detect_metales()
            if cont == 10:
                sens_amp()
            if cont == 20:
                cayo_algo()
            if cont == 30:
                cayo_metal()
            if cont == 40:
                comunicar()
        display.text(font,">",0,cont,3)
        display.text(font,"_ Sens. Ind.",20,0)
        display.text(font,"_ Sens. Amp.",20,40)
        display.text(font,"_ Cayo algo?",20,80)
        display.text(font,"_ Cayo metal?",20,120)
        display.text(font,"_ Comunicar",20,160)
start_up()
sleep(2)
main_menu()
'''