# -*- coding-utf-8 -*-
from flask import Flask, request, url_for, render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list/')
def list():
    return render_template('list.html')

@app.route('/project/<project_id>/')
def project(project_id):
    return render_template('project.html' + project_id)

@app.route('/techniques/')
def techniques():
    return render_template('techniques.html')

@app.route('/search/')
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run()
