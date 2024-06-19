from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'

from . import lenguaje,category
app.register_blueprint(lenguaje.bp)
app.register_blueprint(category.bp)
