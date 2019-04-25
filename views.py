from app import app
from flask import render_template


@app.route('/')
def home():
    name  = 'Alex'
    return render_template('home.html', name=name)
