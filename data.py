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
