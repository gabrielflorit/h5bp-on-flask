import os
import datetime
from myApp import app
from flask import render_template, send_from_directory

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


def versioning():
    return datetime.date.today().strftime('%y%m%d')

