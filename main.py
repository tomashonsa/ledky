from time import sleep
import machine
pin0 = machine.Pin(0, machine.Pin.IN)
pin1 = machine.Pin(1, machine.Pin.OUT)


while True:
    status2 = pin0.value()
    if status2==True:
        pin1.toggle()
        sleep(0.3)
        if status2==False:
            pin1.toggle()
    status1 = pin0.value()
    if status1==True:
        for x in range(2):
            pin1.value(1)
            sleep(0.2)
            pin1.value(0)
            sleep(0.2)

