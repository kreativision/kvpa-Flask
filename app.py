from flask import Flask, render_template, url_for, request, session, logging, redirect, flash
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker

# will use later!
# from passlib.hash import sha256_crypt 

app = Flask(__name__)
# engine = create_engine("mysql+pymysql://root:dbRootKVPA@localhost/kv_schema")
# db=scoped_session(sessionmaker(bind=engine))


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/sign-up')
def signUp():
    return render_template('sign-up.html')


if __name__ == '__main__':
    app.run(debug=True)
