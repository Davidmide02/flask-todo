# print("Hello")
from flask import Flask, render_template
from flask.sqlalchemy import SQLAlchemy
# from flask_sqlalchemy import SQLAlchemy
# import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def add():
    return "About us"


if __name__=="_main_":
    app.run(debug=True)