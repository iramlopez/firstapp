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

#Returning a template page
@app.route('/myapp')
def myapp():
    return render_template('index.html')

#Returining a page with data request
@app.route('/myapp/<string:room>')
def myapp_rooms(room):
    return render_template('rooms.html',room=room)

if __name__== "__main__":
    app.run(debug=True)