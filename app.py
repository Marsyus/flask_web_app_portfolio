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

if __name__ == '__main__':
    app.run(debug=True)
