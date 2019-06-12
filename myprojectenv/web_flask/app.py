#!/usr/bin/env python3
#  user class

from flask import Flask, render_template, jsonify, redirect, url_for, request
from models import storage
import models
import json

app = Flask(__name__)
app.url_map.strict_slashes = False
host = '127.0.0.1'
host = '192.168.33.10'

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
        objs = storage.query("User")
        for obj in objs:
            if uname in obj.__dict__.values():
                flag = 1
                match = obj
        if flag == 0:
            return render_template('index.html')
    return render_template('landing.html', user_info=match)

@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    """ find borrowers page """
    borrowers = None
    if request.method == 'POST':
        params = request.form
        interest = params['interest']
        objs = storage.query("Borrower", 2)
    return render_template('borrow.html', objs=objs)

@app.route('/lend', methods=['GET'])
def lend():
    return render_template('lend.html')

if __name__ == "__main__":
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.register_error_handler(404, page_not_found)
    app.run(host=host, port=5000, debug=True)
