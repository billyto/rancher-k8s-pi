from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_afrika():
    return 'Hello Afrika - Tell me how you\'re doin\'!'
