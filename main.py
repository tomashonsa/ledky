import machine
Pin1 = machine.Pin(0, machine.Pin.IN)
pin2 = machine.Pin(1, machine.Pin.OUT)
while True:
    status = Pin1.value()
    if Pin1 == True:
        Pin1.value(1)
    else:
        Pin1.value(0)