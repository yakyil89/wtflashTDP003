import json

def load(name):
    """Loads a json file and returns the result."""
    with open(name, 'r') as json_file:
        data = json.load(json_file)
    return data


print load('data.json')
