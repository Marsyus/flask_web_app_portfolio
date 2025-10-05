from flask import Flask, render_template, request 

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

if __name__ == '__main__':
    app.run(debug=True)
