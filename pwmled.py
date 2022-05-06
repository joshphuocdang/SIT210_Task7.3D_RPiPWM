from gpiozero import DistanceSensor
from gpiozero import PWMLED
from time import sleep
import RPi.GPIO as GPIO
 
 
led = PWMLED(18)
sensor = DistanceSensor(23,24)

try:
    while (True):
        dis = sensor.distance * 100
        print('Distance: ', dis)
        if dis < 20.0 and dis > 18:
            led.value = 0.2
            sleep(0.5)
        elif dis < 18.0 and dis > 15:
            led.value = 0.4
            sleep(0.5)
        elif dis < 15.0 and dis > 10.0:
            led.value = 0.6
            sleep(0.5)
        elif dis < 10.0:
            led.value = 1
            sleep(0.5)
        else:
            led.value = 0
            sleep(0.5)
        
except KeyboardInterrupt:
    GPIO.cleanup()
            
         