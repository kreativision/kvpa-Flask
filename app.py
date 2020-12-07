from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/sign-up')
def signUp():
    return render_template('sign-up.html')


if __name__ == '__main__':
    app.run(debug=True)
