from flask import Flask, request, render_template, jsonify
import RPi.GPIO as GPIO
from config import Config
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
    config=Config()
    dinamic_navbar=config.getNavigationBar()
    return render_template('mainpage.html', navbar=dinamic_navbar)

@app.route('/home')
def home():
    config=Config()
    rooms=config.getRooms()
    print(rooms)
    return render_template('home.html',rooms=rooms)


@app.route('/community', methods=['GET','POST'])
def community():
    return render_template('community.html')

@app.route('/switches', methods=['GET','POST'])
def switches():
    setup_switches = {
        'kitchen': 11,
        'livingroom': 13,
        'bedroom': 15,
        'lamp1': 17,
        'lamp2': 19
    }
    if request.method=='POST':
        device=request.form['port']
        print(device)
        try:
            print("Value is an int")
            val=int(device)
            print(device)
            switches={
                '1':11,
                '2':13,
                '3':15,
                '4':17,
                '5':19
            }
        except ValueError:
            print("Value is a string")
            print(device)
            switches={
                'kitchen':11,
                'livingroom':13,
                'bedroom':15,
                'lamp1':17,
                'lamp2':19
            }
        print("Setting the switch")
        print(switches[device])

    print(setup_switches)
    return render_template('rooms.html', switches=setup_switches)

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0")
