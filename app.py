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

if __name__ == '__main__':
    app.run(debug=True)
