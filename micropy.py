form machine import Pin
import time
led=(15,Pin.OUT)

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)