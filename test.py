import RPi.GPIO as GPIO
import time
from socketIO_client import SocketIO, LoggingNamespace

GPIO.setmode(GPIO.BOARD) # Set board mode to BROAD

GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(11,GPIO.OUT) 
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

print("Program Started")
while True:
      button_state=GPIO.input(16)
      button_state2=GPIO.input(18)
      button_state3=GPIO.input(22)  
      if button_state == False:
        print("Button Pressed")
        GPIO.output(11,True)
        #socketIO.send("Alert: Panic Button in Gym")
        #socketIO.wait(seconds=1)
        #time.sleep(0.2)
        GPIO.output(11,False)
      elif button_state2 == False:
        print("Button 2 Pressed")
        GPIO.output(13,True)
        #socketIO.send("Alert: Emergency Assistance Needed in Gym")
        #socketIO.wait(seconds=1)
        #time.sleep(0.2)
        GPIO.output(13,False)
      elif button_state3 == False:
	print("Button 3 Pressed")
	GPIO.output(15,True)
	#socketIO.send("Alert: Thread in Place deploy Shield") 
        #socketIO.wait(seconds=1)
	#time.sleep(0.2)
	GPIO.output(15,False)
      else:
        pass	
      
