from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world!"

@app.route('/uni')
def home_12():
    return "Hello Universe!"

@app.route('/user/<username>')
def home_123(username):
    return "Hello %s!" % username

@app.route('/form')
@app.route('/form/<name>')
def form_(name=None):
    return render_template('form.html', name=name)

if (__name__ == '__main__'):
    app.run()