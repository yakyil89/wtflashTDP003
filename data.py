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
    return len(db)

def get_project(db, id):
    for i in range(len(db)):
        if db[i]["project_no"] == id:
            return db[i]
    return

#for i in load('data.json'):
#    print i["project_no"]

print get_project(load('data.json'), 2)
print get_project_count(load('data.json'))
print load('data.json')
