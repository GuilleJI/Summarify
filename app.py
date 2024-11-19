from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_word(): 
    return 'Hello, World!'