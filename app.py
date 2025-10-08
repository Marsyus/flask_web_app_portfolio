from flask import Flask, render_template, request 
from math import pi
import random


app = Flask(__name__)


# HOME
@app.route('/')
def home():
    return render_template('index.html', header_title="Home Page")


# PROFILE
@app.route('/profile')
def profile():
    return render_template('profile.html', header_title="Profile")


# CONTACT
@app.route('/contact')
def contact():
    return render_template('contact.html', header_title="Contact")


# PROGRAMMING WORKS
@app.route('/works')
def works():
    return render_template('works.html', header_title="Programming Works")


# TO UPPERCASE
@app.route('/to-uppercase', methods=['GET', 'POST'])
def to_uppercase():
    result = None
    if request.method == 'POST':
        try:
            input_string = request.form.get('inputString', '')
            result = input_string.upper()
        except ValueError:
            result = "Invalid input. Please enter a string."
    return render_template('to-uppercase.html', 
                           result=result, 
                           header_title="Convert to Uppercase"
                           )


# AREA OF CIRCLE
@app.route('/area-of-circle', methods=['GET', 'POST'])
def area_of_circle():
    result, error = None, None
    if request.method == 'POST':
        try:
            input_radius = float(request.form.get('inputRadius', 0))
            result = pi * input_radius ** 2
        except ValueError:
            error = "Invalid input. Please enter a number."
    return render_template('area-of-circle.html', 
                           result=result, 
                           error=error, 
                           header_title="Area of Circle"
                           )


# AREA OF TRIANGLE
@app.route('/area-of-triangle', methods=['GET', 'POST'])
def area_of_triangle():
    result, error = None, None
    if request.method == 'POST':
        try:
            input_base = float(request.form.get('inputBase', 0))
            input_height = float(request.form.get('inputHeight', 0))
            result = input_base * input_height * 1/2
        except ValueError:
            error = "Invalid input. Please enter a number."
    return render_template('area-of-triangle.html', 
                           result=result, 
                           error=error, 
                           header_title="Area of Triangle"
                           )


# ROCK PAPER SCISSORS 
@app.route('/rock-paper-scissors')
def rock_paper_scissors():
    player = request.args.get('choice')
    opponent = None
    result = None
    with open('static/score.txt', 'r') as scr:
        scores = scr.read()
        player_scr, opponent_scr = map(int, scores.split(','))

    if player:
        opponent = random.choice(['rock', 'paper', 'scissors'])
        if player == opponent:
            result = "It's a tie!"
        elif (player == 'rock' and opponent == 'scissors') or \
            (player == 'paper' and opponent == 'rock') or \
            (player == 'scissors' and opponent == 'paper'):
            result = "You won!"
            player_scr += 1
        else:
            result = "You lost!"
            opponent_scr += 1

    with open('static/score.txt', 'w') as scr:
        scr.write(f"{player_scr},{opponent_scr}")

    return render_template('rock-paper-scissors.html', 
                           player=player, 
                           opponent=opponent, 
                           player_scr=player_scr, 
                           opponent_scr=opponent_scr, 
                           result=result, 
                           header_title="Rock Paper Scissors"
                           )


if __name__ == '__main__':
    app.run(debug=True)
