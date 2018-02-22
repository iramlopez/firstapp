from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time
app = Flask(__name__)

# chan_list=[11,13,15]
# GPIO.setup(chan_list,GPIO.OUT)

GPIO.setmode(GPIO.BOARD) # Set board mode to Broadcom
GPIO.setup(11, GPIO.OUT) # set up pin 17
GPIO.setup(13, GPIO.OUT) # Set up pin 22
GPIO.setup(15, GPIO.OUT) # Set up pint 27
# GPIO.setup(port, GPIO.IN)


# Use flask to create a basic web server
# @ Signifies a decorator - way to wrap a function and modifying its behavior
# Connectiong a url token with a page
# By default flask uses templates file directory for the templates
# By default flask uses static file directory for the static content css, js, images

#Returning a basic response
@app.route('/')
def index():
    return "Hello World"

@app.route('/switches', methods=['GET','POST'])
def switches():
    if request.method=='POST':
        device=request.form['port']
        print(device)

        try:
            print("Value is an int")
            val=int(device)
            print(device)
            switcher={
                '1':11,
                '2':13,
                '3':15
            }
        except ValueError:
            print("Value is a string")
            print(device)
            switcher={
                'kitchen':11,
                'livingroom':13,
                'bedroom':15
            }
        print("Setting the switch")
        print(switcher[device])
        func=switcher.get(switcher[device], lambda: GPIO.output(switcher[device], GPIO.HIGH))
    return render_template('switches.html')

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0")
