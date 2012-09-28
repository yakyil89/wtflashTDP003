#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module makes out the data layer of the portfolio project in the
course TDP003 at Innovativ Programmering, Linköping's University, Sweden
"""

import json

def load(name):
    """Reads a given file and returns it's content. Returns None if no file
    was found."""
    try: 
        with open(name, 'r') as json_file:
            data = json.load(json_file)
            return data
    # If the file doesn't exist, return None.
    except:
        return

def get_project_count(db):
    """Returns the number of objects in a given list."""
    return len(db)

def get_project(db, id):
    """Returns a dictionary containing the project with a given id."""
    for i in db:
        if i["project_no"] == id:
            return i
    return

def get_techniques(db):
    """Returns a list of all techniques used, ordered alphabetically."""
    # Use set instead of list to avoid duplets
    the_set = set()
    for i in db:
        for t in i["techniques_used"]:
            the_set.add(t)
    # Convert the set to a list and sort it.
    lis = list(the_set)
    lis.sort()
    return lis

def get_technique_stats(db):
    """Reads a list of projects and returns a dictionary with stats for the
    used techniques."""
    # Variable that holds all techniques used.
    techs = get_techniques(db)
    # Creates an empty dictionary to hold the technique statistics.
    dic = {}
    # Iterates through all techniques.
    for t in techs:
        name = []
        id = []
        # Iterates through all projects for every available technique.
        for i in db:
            lis = []
            if t in i["techniques_used"]:
                # Fills a list with the names of all projects usin the technique
                name.insert(0, i["project_name"])
                # Fills a list with the IDs of all projects usin the technique.
                id.insert(0, i["project_no"])
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
    # Return all projects if search == None
    if search == None:
        lis = db
        return lis
    if isinstance(search, (unicode, str)):
        #search = search.upper()
        for i in range(len(db)):
            for p in db[i]:
                # Without this line the code will fail when it comes to an int.
                if isinstance(db[i][p], (unicode, int, str)):
                    project_upper = unicode(db[i][p])
                    # Can't convert in the previous step since it might be int.
                    project_upper = project_upper.upper()
                    try:
                        search = unicode(search, 'utf-8')
                    except: pass
                    search = search.upper()
                    if search in project_upper:
                        lis.append(db[i])
                        # Break the loop to prevent duplets.
                        break
    return lis

def free_search_limited(db, search, search_fields):
    """Free search with limited search fields to search in."""
    lis = []
    # Return all projects if search == None
    if search == None:
        lis = db
        return lis
    if isinstance(search, (unicode, str)):
        for i in range(len(db)):
            for p in search_fields:
                # Without this line the code will fail when it comes to an int.
                if isinstance(db[i][p], (unicode, int, str)):
                    project_upper = unicode(db[i][p])
                    # Can't convert in the previous step since it might be int.
                    project_upper = project_upper.upper()
                    try:
                        search = unicode(search, 'utf-8')
                    except: pass
                    search = search.upper()
                    if search in project_upper:
                        lis.append(db[i])
                        # Break the loop to prevent duplets.
                        break
    return lis

def search(db, sort_by=u'start_date', sort_order=u'desc', techniques=None,
           search=None, search_fields=None):
    """Given a set of parameters, this function searches through the matching
    project. Returns a list of the projects and their attributes."""

    # Return empty list if search or search_fields is empty.
    if search_fields == '':
        return
    if search == '':
        return

    # Creates a list to hold the projects
    lis = []
    if search_fields == None:
        lis = free_search(db, search)
    else:
        lis = free_search_limited(db, search, search_fields)
    # Return empty list if the search value didn't match anything.
    if lis == '':
        return
        
    # Creates a list to hold the projects matching both search and techniques.
    tech_lis = []
    # Pass in all objects from search if techniques == None.
    if techniques == None:
        tech_lis = lis
    else:
        # If techniques is empty, assign all techniques available to it.
        if techniques == []:
            techniques = get_techniques(db)
        # Iterate through the list and append the value to tech_lis if
        # it contains a technique from the techniques list.
        for i in range(len(lis)):
            for t in range(len(techniques)):
                if techniques[t] in lis[i][u'techniques_used']:
                    tech_lis.append(lis[i])
                    # Break to avoid duplets.
                    break
    
    # --Order the list--
    # Creates a list to hold the values to sort.
    sort_key = []
    sorted_lis = []
    for i in range(len(tech_lis)):
        sort_key.append(tech_lis[i][sort_by])
    sort_key.sort() 
    if sort_order == 'desc':
        sort_key.reverse()

    for k in range(len(sort_key)):
        for l in range(len(tech_lis)):
            # Appends objects from tech_lis to sorted_lis in sorted order.
            if tech_lis[l][sort_by] == sort_key[k]:
                sorted_lis.append(tech_lis[l])
    return sorted_lis

