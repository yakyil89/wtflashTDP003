# -*- coding-utf-8 -*-
"""Server module that makes the website able to run, also redirects the
links on the pages to the right pages."""

from flask import Flask, request, url_for, render_template
import data

# Database (data.json).
db = data.load('data.json')

# List of all used techniques.
all_techniques = data.get_techniques(db)

# Variabel to run the website.
app = Flask(__name__)
app.debug = True

import datetime
def log(page, data=None):
    """Takes a page name and an optional data parameter.
    Saves the result nicely formatted in log.log (creates the log file if
    it doesn't allready exist)."""
    date = datetime.datetime.now()
    date = date.strftime("%Y-%M-%D %H:%M")
    if data:
        log_text = date + '\t' + 'accessed: ' + page + '\t' + 'with ' + data + '\n'
    else:
        log_text = date + '\t' + 'accessed: ' + page + '\n'
    with open('log.log', 'a') as log:
        log.write(log_text)


@app.route('/')
def index():
    """Redirects to index.html"""
    log('index.html')
    return render_template('index.html', data=data, db=db)

@app.route('/list/')
def list():
    """Redirects to list.html"""
    log('list.html')
    sorted_db = data.order(db)
    return render_template('list.html', data=data, db=sorted_db)

@app.route('/project/<int:project_id>/')
def project(project_id):
    """Redirects to project.html and sends the project with the ID given in the URL"""
    log('project.html', ('id: ' + str(project_id)))
    project = data.get_project(db, project_id)
    if not project_id in data.get_ids(db):
        project = None
    return render_template('project.html', data=data, db=db, project=project)

@app.route('/techniques/')
def techniques():
    """Redirects to techniques.html"""
    log('techniques.html')
    techniques = data.get_techniques(db)
    return render_template('techniques.html', all_techniques=all_techniques, data=data, techniques=techniques, db=db)

@app.route('/search/', methods=['POST'])
def search():
    """Redirects to search.html and sends a list with projects that's given from the search form"""
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
    
    logtext = [key, search_fields, techniques, sort_by, sort_order]
    log('search.html', ('parameters: ' + str(logtext)))
    
    lst = data.search(db, search=key, search_fields=search_fields, techniques=techniques, sort_by=sort_by, sort_order=sort_order)
    return render_template('search.html', data=data, db=db, lst=lst)
    
@app.errorhandler(404)
def page_not_found(e):
    """Handles 404-errors"""
    return render_template('404.html', data=data, db=db), 404

@app.errorhandler(500)
def page_not_found(e):
    """Handles 500-errors"""
    return render_template('500.html', data=data, db=db), 500

if __name__ == '__main__':
    app.run()
