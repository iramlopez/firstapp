from flask import Flask, request, render_template
app = Flask(__name__)

# Use flask to create a basic web server
# @ Signifies a decorator - way to wrap a function and modifying its behavior
# Connectiong a url token with a page
# By default flask uses templates file directory for the templates
# By default flask uses static file directory for the static content css, js, images

#Returning a basic response
@app.route('/')
def index():
    return "Hello World"

@app.route('/juangarcia')
def myfunction():
    return render_template('juangarcia.html')

#Returning a template page
@app.route('/myapp')
def myapp():
    return render_template('index.html')

@app.route('/alejandros')
def myFunction():
    return render_template('alejandros.html')

#Returining a page with data request
@app.route('/myapp/<string:room>')
def myapp_rooms(room):
    return render_template('rooms.html',room=room)

@app.route("/myjilhouse")
def myjilfunction():
    button1='on'
    button2='off'
    devices={'button1':'on',
             'button2':'off',
             'button3':'on'
             }
    return render_template("jil_index.html", devices=devices)

@app.route("/chris")
def myFunction2():
    return render_template("chris.html")

@app.route("/HIram'sTinyHouse")
def hiramFunction():
    return render_template("HIram'sTinyHouse.html")


if __name__== "__main__":
    app.run(debug=True)

