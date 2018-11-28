import RPi.GPIO as GPIO
import time
from socketIO_client import SocketIO, LoggingNamespace

GPIO.setmode(GPIO.BOARD) # Set board mode to BROAD
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT) #LED to GPIO24

try:
    while True:
         button_state = GPIO.input(23)
         if button_state == False:
             GPIO.output(24, True)
             with SocketIO('127.0.0.1', 5000, LoggingNamespace) as socketIO:
                 socketIO.send("Sending Another set Of Data")
                 socketIO.wait(seconds=1)
             time.sleep(0.2)
         else:
             GPIO.output(24, False)
except:
    GPIO.cleanup()
