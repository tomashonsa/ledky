from time import sleep
import machine
pin0 = machine.Pin(0, machine.Pin.IN)
pin1 = machine.Pin(1, machine.Pin.OUT)
pin2 = machine.Pin(2, machine.Pin.OUT)
pin3 = machine.Pin(3, machine.Pin.OUT)
pin4 = machine.Pin(4, machine.Pin.OUT)
pin5 = machine.Pin(5, machine.Pin.OUT)

while True:
    status = pin0.value()
    if status == True:
        for x in range(5):
            pin1.value(1)
            pin3.value(1)
            pin5.value(1)
            sleep(1)
            pin1.value(0)
            pin3.value(0)
            pin5.value(0)
            pin2.value(1)
            pin4.value(1)
            sleep(1)
            pin2.value(0)
            pin4.value(0)
    else:
        pin1.value(0)