"""This was a demo of Flask at Introduction to TCP/IP and InfoSec Concepts 101"""

from flask import Flask
app = Flask(__name__)


counter = 0

@app.route("/")
def hello():
    global counter
    counter += 1
    return "Hello World you are visitor number {0}".format(counter)
