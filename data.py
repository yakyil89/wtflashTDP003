#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

def load(name):
    """Reads a given file and returns it's content. Returns None if no file
    was found."""
    try: 
        with open(name, 'r') as json_file:
            data = json.load(json_file)
            return data
    except:
        return

def get_project_count(db):
    """Returns the number of objects in a given list."""
    return len(db)

def get_project(db, id):
    """Returns a dictionary containing the project with a given id."""
    for i in range(len(db)):
        if db[i]["project_no"] == id:
            return db[i]
    return

def get_techniques(db):
    """Returns a list of all techniques used, ordered alphabetically."""
    the_set = set()
    for i in range(len(db)):
        for t in range(len(db[i]["techniques_used"])):
            the_set.add(db[i]["techniques_used"][t])
    lis = list(the_set)
    lis.sort()
    return lis

def get_technique_stats(db):
    """Collects and returns statistics for all the techniques used in the
    project list."""
    # Variable that holds all techniques used.
    techs = get_techniques(db)
    # Creates an empty dictionary to hold the technique statistics.
    dic = {}
    # Iterates through all techniques.
    for t in techs:
        name = []
        id = []
        # Iterates through all projects for every available technique.
        for i in range(len(db)):
            lis = []
            if t in db[i]["techniques_used"]:
                # Fills a list with the names of all projects usin the technique
                name.insert(0, db[i]["project_name"])
                # Fills a list with the IDs of all projects usin the technique.
                id.insert(0, db[i]["project_no"])
            # Iterates through all names saved in the previous step.    
            for l in range(len(name)):
                # Appends all id/name pairs to a list.
                lis.append({u'id': id[l], u'name': name[l]})
            # Adds the list to the dictionary, with the technique as key.
            dic[t] = lis
    return dic

def free_search(db, search):
    """Free search."""
    lis = []
    if search == None:
        lis = db
        return lis
    if isinstance(search, unicode):
        search = search.upper()
        for i in range(len(db)):
            for p in db[i]:
                # Without this line the code will fail when it comes to an int.
                if isinstance(db[i][p], (unicode)):
                    project_upper = db[i][p].upper()
                    if search in project_upper:
                        lis.append(db[i])
                        break
    return lis

def free_search_limited(db, search, search_fields):
    """Free search with limited search fields."""
    lis = []
    if search == None:
        lis = db
        return lis
    if isinstance(search, (unicode, str)):
        search = search.upper()
        for i in range(len(db)):
            for p in search_fields:
                # Without this line the code will fail when it comes to an int.
                if isinstance(db[i][p], (unicode, int, str)):
                    project_upper = unicode(db[i][p])
                    try:
                        search = unicode(search, 'utf-8')
                    except: pass
                    search = search.upper()
                    if search in project_upper:
                        lis.append(db[i])
                        break
    return lis

def search(db, sort_by=u'start_date', sort_order=u'desc', techniques=None, search=None,
           search_fields=None):
    """Given a set of parameters, this function searches through the matching project.
    Returns a list of the projects and their attributes."""

    if search_fields == '':
        return
    if search == '':
        return

    lis = []
    if search_fields == None:
        lis = free_search(db, search)
    else:
        lis = free_search_limited(db, search, search_fields)
    if lis == '':
        return
        

    tech_lis = []
    
    # Sorts out the techniques.
    if techniques == None:
        tech_lis = lis
    else:
        if techniques == []:
            techniques = get_techniques(db)
        for i in range(len(lis)):
            for t in range(len(techniques)):
                if techniques[t] in lis[i][u'techniques_used']:
                    tech_lis.append(lis[i])
                    break
    
    # Order the list.
    sort_key = []
    sorted_lis = []
    for i in range(len(tech_lis)):
        sort_key.append(tech_lis[i][sort_by])
    sort_key.sort()
    if sort_order == u'desc':
        sort_key.reverse()

    for k in range(len(sort_key)):
        for l in range(len(tech_lis)):
            if tech_lis[l][sort_by] == sort_key[k]:
                sorted_lis.append(tech_lis[l])
    return sorted_lis
