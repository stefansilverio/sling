#!/usr/bin/env python3
#  user class

from flask import Flask, render_template, jsonify, redirect, url_for, request
from models import storage
import models
import json

app = Flask(__name__)
app.url_map.strict_slashes = False
host = '127.0.0.1'
host = '55.55.55.5'

def page_not_found(e):
    """ 404 error page for nonexistent routes """
    return jsonify({'error': "Not found"}), 404


@app.route("/", methods=['GET'])
def login():
    """ render login homepage """
    return render_template('index.html')

@app.route("/landing", methods=['POST'])
def landing():
    """landing page"""
    flag = 0
    if request.method == 'POST':
        uname = request.form.get('email')
        print(uname)
        objs = storage.query("User")
        for obj in objs:
            if uname in obj.__dict__.values():
                print("OBJ TYPE {}".format(obj))
                print(obj.__dict__)
                user = obj.__dict__
                print(user.first_name)
                flag = 1
            if flag == 1:    
                return render_template('index.html')
    return render_template('landing.html', user_info=obj.__dict__)

@app.route('/burrow', methods=['GET'])
def burrow():
    return '<h1> Burrow, Here!</h1>'

@app.route('/lend', methods=['GET'])
def lend():
    return '<h1> Lend, Here!</h1>'

if __name__ == "__main__":
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.register_error_handler(404, page_not_found)
    app.run(host=host, port=5000, debug=True)
