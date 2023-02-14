from flask import Flask, render_template , redirect , request
from flask_mysqldb import MySQL


app = Flask(__name__)



mysql = MySQL(app)

@app.route('/')
def index():
    msg = ''
    return render_template('index.html', msg=msg)
