import RPi.GPIO as GPIO
import time

SENSOR_PIN=37


GPIO.setmode(GPIO.BOARD) # Set board mode to BROAD
GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.setup(11, GPIO.OUT) #LED to GPIO24

print("Entering Program")
time.sleep(2)
print("Starting Program")

def my_callback(channel):
	print("Momevent Detected")
	GPIO.output(11,True)
	time.sleep(0.2)
	GPIO.output(11,False)

try:
    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=my_callback)
    while True:
	pass
	#print("Before sleep");
	#time.sleep(0.1)
	#print("After Sleep");
except KeyboardInterrupt:
    print("Finish")
GPIO.cleanup()




