#!/usr/bin/env python3
#  user class

from flask import Flask, render_template, jsonify
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False
host = '127.0.0.1'
host = '55.55.55.5'

def page_not_found(e):
    """ 404 error page for nonexistent routes """
    return jsonify({'error': "Not found"}), 404


@app.route("/")
def login():
    """ render login homepage """
    return render_template('index.html')

@app.route("/user")
def landing():
    return render_template('landing.html')

@app.route('/lend', methods=['GET'])
def lend():
    return '<h1> Lend, Here!</h1>'

if __name__ == "__main__":
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.register_error_handler(404, page_not_found)
    app.run(host=host, port=5000, debug=True)
