import RPi.GPIO as GPIO
import time
import httplib, urllib

GPIO.setmode(GPIO.BOARD) # Set board mode to BROAD
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
params = urllib.urlencode({'number': 12524, 'type': 'issue', 'action': 'show'})

headers = {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}

while True:
	input_state==GPIO.input(12)
	if input_state==False:
		print("Button Pressed")
		conn = httplib.HTTPConnection("localhost:5000")
		conn.request("POST", "", params, headers)
		response = conn.getresponse()
		print response.status, response.reason
		data = response.read()
		data
		'Redirecting to <a href="http://bugs.python.org/issue12524">http://bugs.python.org/issue12524</a>'
		conn.close()
		time.sleep(0.2)

