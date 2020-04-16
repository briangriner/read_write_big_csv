#!/bin/python3
# make.sh - run consumer_complaints.py to read ../input/complaints.csv and create ../output/report.csv

python3 -u /src/consumer_complaints.py > consumer_complaints.py.log 2>&1 
