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

print get_project_count(load('data.json'))
print load('data.json')
