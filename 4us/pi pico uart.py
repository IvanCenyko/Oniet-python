from machine import UART, Pin
import json
from time import sleep
import _thread

uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))
data = None
lock = _thread.allocate_lock()

def uartread():
    while 1:
        data = uart.read()
        if data:
            data = json.loads(data.decode('utf8'))
        lock.acquire()



_thread.start_new_thread(uartread, ())

while 1:
    lock.release()
    global data
    print(data)
    
'''
while 1:
    data = uart.read()
    if data:
        data = data.decode('utf8')
        data = json.loads(data)
        print(data)
        print(data['type'])
        
        
while 1:
    if data:
    ...
    data = None


'''