from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/dojo.html')
def dojo():
    return render_template('dojo.html')
#
@app.route('/new.html')
def new():
    # name = request.form['name']
    # email = request.form['email']
    # comment = request.form['comment']
    return render_template('new.html')

@app.route('/ninjas.html')
def ninjas():
    return render_template('ninjas.html')

app.run(debug=True)
