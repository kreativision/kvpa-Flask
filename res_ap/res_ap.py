from flask import Blueprint
from flask.templating import render_template

res_ap = Blueprint('res_ap',__name__,
    template_folder='templates',
    static_folder='assets',
    static_url_path='/assets')

@res_ap.route('/')
@res_ap.route('/home')
def index():
    return render_template('r_ap.index.html', title='Introduction')

@res_ap.route('/edu')
def edu():
    return render_template('r_ap.edu.html', title='Education')

@res_ap.route('/exp')
def exp():
    return render_template('r_ap.exp.html', title='Experience')

@res_ap.route('/skills')
def skills():
    return render_template('r_ap.skills.html', title='Skills')

@res_ap.route('/projects')
def projects():
    return render_template('r_ap.projects.html', title='Projects')
    
@res_ap.route('/hobbies')
def hobbies():
    return render_template('r_ap.hobbies.html', title='Hobbies & Interests')

