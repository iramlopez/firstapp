from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
import RPi.GPIO as GPIO
import os.path as Path
from config import Config
import time
from functools import update_wrapper
app = Flask(__name__)
app.config['SECRET_KEY']='THISISTHESECRETKEY'
cors = CORS(app,support_credentials=True)
app.config['CORS_HEADERS'] = 'application/json'
# chan_list=[11,13,15]
# GPIO.setup(chan_list,GPIO.OUT)
GPIO.setmode(GPIO.BOARD) # Set board mode to BROAD
GPIO.setup(11, GPIO.OUT) # set up pin 11
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT) # Set up pin 13
GPIO.setup(29, GPIO.OUT) # Set up pint 15
GPIO.setup(31,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
# GPIO.setup(port, GPIO.IN)
# Use flask to create a basic web server
# @ Signifies a decorator - way to wrap a function and modifying its behavior
# Connectiong a url token with a page
# By default flask uses templates file directory for the templates
# By default flask uses static file directory for the static content css, js, images
#Returning a basic response

@app.route('/',methods=['GET','POST'])
def index():
    room_name='community'
    print(room_name)
    config=Config()
    rooms=config.getRooms()
    room=rooms.get(room_name)
    dinamic_navbar=config.getRooms()
    return render_template('index.html',navigation=rooms, path=request.url_root,room=room)

#Returning a basic response
@app.route('/<room_name>',methods=['GET','POST'])
def rooms(room_name):
    print (request.url_root)
    print(room_name)
    config=Config()
    rooms=config.getRooms()
    room=rooms.get(room_name)
    dinamic_navbar=config.getRooms()
    return render_template('index.html',navigation=rooms, path=request.url_root,room=room)

#Setting the Swith on/off
@app.route('/set/switch',methods=['POST'])
@cross_origin(support_credentials=True)
def setswitch():
    switch=request.get_json()
    print(switch.get('port'))
    print(switch.get('status'))
    port=int(switch.get('port'))
    stat=int(switch.get('status'))
    GPIO.output(port,stat)
    return (jsonify({"response":"done"})),200

@app.route('/cleanup',methods=['GET','POST'])
def cleanup():
    room_name='community'
    GPIO.cleanup()
    print (request.url_root)
    print(room_name)
    config=Config()
    rooms=config.getRooms()
    room=rooms.get(room_name)
    dinamic_navbar=config.getRooms()
    return render_template('index.html',navigation=rooms, path=request.url_root,room=room)

if __name__== "__main__":
    app.run(debug=True,host='0.0.0.0')
