from flask import Flask, render_template, url_for, request, session, logging, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from dbConfig import db
from forms import RegistrationForm, LoginForm
from markupsafe import Markup


app = Flask(__name__)
app.config['SECRET_KEY'] = '72a11398ef34db96b2cc7293218cbf49'
db_config = f'{db.category}://{db.user}:{db.pwd}@{db.url}:{db.port}/{db.name}'
app.config['SQLALCHEMY_DATABASE_URI'] = db_config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class member(db.Model):
    ph_no = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(40), unique = True)
    email = db.Column(db.String(40), unique = True)
    password = db.Column(db.String(20))

    def __repr__(self):
        return f'Member({self.first_name})'



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        message = Markup(f'Account Created for <strong>{form.username.data}</strong>!')
        flash(message, category='success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registration', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@kv.com' and form.password.data == 'password':
            flash(f'You have been logged in!', category='primary')
            return redirect(url_for('home'))
        else:
            flash(f'Incorrect Credentials! Please check and try again!', category='danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6174, debug=True) 
    # this config allows for the app to be run on the local network;
    # accessible from the phone/tablet connected to the same WiFi netork as the laptop on which the app is running.

    # to access the dev-server on the phone, follow these steps: 
        # open a terminal => enter command => "ipconfig"
        # look for something similar to => 'IPv4 Address. . . . . . . . . . . : 192.168.XX.XXX'
        # on your phone access the IP => 192.168.XX.XXX:6174 to view the running application.

    # to run the app only in the default localhost:5000 or 127.0.0.1:5000, replace line 'app.run()' with
    # app.run(debug=True)