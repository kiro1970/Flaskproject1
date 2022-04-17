from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html', title="PokeAPI Battler!")

@app.route('/howitworks')
def about():
    return render_template('howitworks.html', title="Learn how to battle!")

@app.route('/letsbattle')
def battle():
    return render_template('letsbattle.html', title="Let's Battle!")


