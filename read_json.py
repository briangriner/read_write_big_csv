#! /usr/bin/python3 -0
# read_json.py - reads json data downloaded from consumer_complaints api and creates a python dict
# no api key so must download rather than requests.get() 

import json

path = '/mnt/chromeos/MyFiles/Downloads/consumer_complaints_data/json/'

filename = path + 'complaints.json'

# load json into python dict
try:
    with open(filename, 'r') as f:
        complaints = json.load(f)
except FileNotFoundError:
    print("Problem loading json file. Check filename and path.")
else:
    print("JSON file loaded. Print check: ", complaints[0])

''' todos:
    1. check correct path for json file on cb - done
    2. Fix memory error: try open(filename, 'a'), readlines(), f.write(save_file)
    
    report strategy:  use dict comprehensions for agg funcs where possible''' 
