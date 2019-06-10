#!/usr/bin/env python
#  user class

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/lend')
def lend():
    return '<h1> Lend, Here!</h1>'

if __name__ == "__main__":
    app.run(host='217.70.184.38', debug=True)
