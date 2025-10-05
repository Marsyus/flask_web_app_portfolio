from flask import Flask, render_template, request 
from math import pi


app = Flask(__name__)


# HOME
@app.route('/')
def home():
    return render_template('index.html')


# PROFILE
@app.route('/profile.html')
def profile():
    return render_template('profile.html')


# PROGRAMMING WORKS
@app.route('/works.html')
def works():
    return render_template('works.html')


# TO UPPERCASE
@app.route('/to-uppercase.html', methods=['GET', 'POST'])
def to_uppercase():
    result = None
    if request.method == 'POST':
        try:
            input_string = request.form.get('inputString', '')
            result = input_string.upper()
        except ValueError:
            result = "Invalid input. Please enter a string."
    return render_template('to-uppercase.html', result=result)


# AREA OF CIRCLE
@app.route('/area-of-circle.html', methods=['GET', 'POST'])
def area_of_circle():
    result, error = None, None
    if request.method == 'POST':
        try:
            input_radius = float(request.form.get('inputRadius', 0))
            result = pi * input_radius ** 2
        except ValueError:
            error = "Invalid input. Please enter a number."
    return render_template('area-of-circle.html', result=result, error=error)


# AREA OF TRIANGLE
@app.route('/area-of-triangle.html', methods=['GET', 'POST'])
def area_of_triangle():
    result, error = None, None
    if request.method == 'POST':
        try:
            input_base = float(request.form.get('inputBase', 0))
            input_height = float(request.form.get('inputHeight', 0))
            result = input_base * input_height * 1/2
        except ValueError:
            error = "Invalid input. Please enter a number."
    return render_template('area-of-triangle.html', result=result, error=error)


if __name__ == '__main__':
    app.run(debug=True)
