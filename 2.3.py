import RPi.GPIO as GPIO
from time import sleep
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
output_channel = [18,23,24,25,8]
input_channel = [20,21]
GPIO.setup(input_channel,GPIO.IN, pull_up_down= GPIO.PUD_UP)
GPIO.setup(output_channel, GPIO.OUT,initial=GPIO.LOW)

try:
    while (1):
        
        if GPIO.input(20)==0:
            GPIO.output(18, True)
            GPIO.output(23,False)
            GPIO.output(24, False)
            GPIO.output(25, False)
            GPIO.output(8, False)
            time.sleep(1)
            GPIO.output(18, False)
            GPIO.output(23,True)
            GPIO.output(24, False)
            GPIO.output(25, False)
            GPIO.output(8, False)
            time.sleep(1)
            GPIO.output(18, False)
            GPIO.output(23,False)
            GPIO.output(24, True)
            GPIO.output(25, False)
            GPIO.output(8, False)
            time.sleep(1)
            GPIO.output(18, False)
            GPIO.output(23,False)
            GPIO.output(24, False)
            GPIO.output(25, True)
            GPIO.output(8, False)
            time.sleep(1)
            GPIO.output(18, False)
            GPIO.output(23,False)
            GPIO.output(24, False)
            GPIO.output(25, False)
            GPIO.output(8, True)
            print("1")
        if GPIO.input(21)==0:
            
            GPIO.output(18, False)
            GPIO.output(23,False)
            GPIO.output(24, False)
            GPIO.output(25, False)
            GPIO.output(8, True)
            time.sleep(1)
            GPIO.output(18, False)
            GPIO.output(23,False)
            GPIO.output(24, False)
            GPIO.output(25, True)
            GPIO.output(8, False)
            time.sleep(1)
            GPIO.output(18, False)
            GPIO.output(23,False)
            GPIO.output(24, True)
            GPIO.output(25, False)
            GPIO.output(8, False)
            time.sleep(1)
            GPIO.output(18, False)
            GPIO.output(23,True)
            GPIO.output(24, False)
            GPIO.output(25, False)
            GPIO.output(8, False)
            time.sleep(1)
            GPIO.output(18, True)
            GPIO.output(23,False)
            GPIO.output(24, False)
            GPIO.output(25, False)
            GPIO.output(8, False)
            print("2")
            
         #if GPIO.input(20) == 1 and GPIO.input(21) ==1:
             #GPIO.output(output_channel, False)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("End")
    

