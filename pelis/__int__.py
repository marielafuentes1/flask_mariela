from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/quien')
def quien():
    return 'echo por mariela fuentes'

