from typing_extensions import runtime
from flask import Flask
app = Flask(__name__)
@app.route('/')
def x():
    return 2
set FLASK_APP=app.py
flask run
