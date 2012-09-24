#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

def load(name):
    """Loads a json file and returns the result."""
    try: 
        with open(name, 'r') as json_file:
            data = json.load(json_file)
            return data
    except:
        return

def get_project_count(db):
    """Returns the length of the list as an int."""
    return len(db)

def get_project(db, id):
    """Returns the dictionary containing the project with a given id."""
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

print get_techniques(load('data.json'))
get_project(load('data.json'), 2)
get_project_count(load('data.json'))
load('data.json')
