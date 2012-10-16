# -*- coding-utf-8 -*-
from flask import Flask, request, url_for, render_template
import data
db = data.load('data.json')

all_techniques = data.get_techniques(db)

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html', data=data, db=db)

@app.route('/list/')
def list():
    sorted_db = data.order(db)
    return render_template('list.html', data=data, db=sorted_db)

@app.route('/project/<int:project_id>/')
def project(project_id):
    project = data.get_project(db, project_id)
    return render_template('project.html', all_techniques=all_techniques, data=data, project=project)

@app.route('/techniques/')
def techniques():
    techniques = data.get_techniques(db)
    return render_template('techniques.html', all_techniques=all_techniques, data=data, techniques=techniques, db=db)

@app.route('/search/', methods=['POST'])
def search():

    key = request.form['key'].encode('UTF-8').upper()
    if key == '':
        key = None

    search_fields = request.form.getlist('search_fields')
    if search_fields == []:
        search_fields = None

    techniques = request.form.getlist('techniques')
    if techniques == []:
        techniques = None

    sort_by = request.form['sort_by']

    sort_order = request.form['sort_order'].encode('UTF-8')

    lst = data.search(db, search=key, search_fields=search_fields, techniques=techniques, sort_by=sort_by, sort_order=sort_order)
    return render_template('search.html', data=data, db=db, lst=lst, sort_order=sort_order)

if __name__ == '__main__':
    app.run()
