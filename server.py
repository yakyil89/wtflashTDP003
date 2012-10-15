# -*- coding-utf-8 -*-
from flask import Flask, request, url_for, render_template
import data
db = data.load('data.json')

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html', data=data, db=db)

@app.route('/list/')
def list():
    sorted_db = data.order(db)
    return render_template('list.html', db=sorted_db)

@app.route('/project/<int:project_id>/')
def project(project_id):
    project = data.get_project(db, project_id)
    return render_template('project.html', project=project)

@app.route('/techniques/')
def techniques():
    techniques = data.get_techniques(db)
    return render_template('techniques.html', techniques=techniques, db=db)

@app.route('/search/')
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run()
