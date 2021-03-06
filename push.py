import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) # Set board mode to BROAD
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.OUT) #LED to GPIO24
print("Entering Program")
try:
    while True:
         button_state = GPIO.input(16)
         if button_state == False:
             GPIO.output(15, True)
             print('Button Pressed...')
             time.sleep(0.2)
         else:
             GPIO.output(15, False)
except:
    GPIO.cleanup()

