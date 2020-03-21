from app import app
#from flask import Flask, request, jsonify
from .doc import *
#import lib.doc

#@app.route('/', methods=['POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return "Hello, World!"

@app.route('/doc', methods=['GET', 'POST'])
def doc():
    return(get_doc())

@app.route('/add', methods=['GET', 'POST'])
def add():
    return(put_doc())
