import RPi.GPIO as GPIO
import time

SENSOR_PIN=37


GPIO.setmode(GPIO.BOARD) # Set board mode to BROAD
GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.setup(11, GPIO.OUT) #LED to GPIO24

print("Entering Program")
time.sleep(2)
print("Starting Program")

def my_callback():
	print("Momevent Detected")
	GPIO.output(11,True)
        time.sleep(2)

while True:
   signal=GPIO.input(SENSOR_PIN)
   if signal==1:
        print("Start")
	my_callback()
        time.sleep(3)
        print("End")
	GPIO.output(11,False)



