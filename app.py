from flask import Flask, render_template, url_for, request, session, logging, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from dbConfig import db
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)
db_config = f'{db.category}://{db.user}:{db.pwd}@{db.url}:{db.port}/{db.name}'
app.config['SQLALCHEMY_DATABASE_URI'] = db_config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class member(db.Model):
    ph_no = db.Column(db.String(40), primary_key=True)
    first_name = db.Column(db.String(40), unique = True)
    last_name = db.Column(db.String(40))
    email = db.Column(db.String(40), unique = True)
    password = db.Column(db.String(20))

    def __init__(self, ph_no, password):
        self.ph_no = ph_no
        self.password = password



@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/sign-up')
def signUp():
    return render_template('sign-up.html')


if __name__ == '__main__':
    app.run(debug=True)
