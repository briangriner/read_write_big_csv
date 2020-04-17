#!/bin/bash
# make.sh - run consumer_complaints.py to read ../input/complaints.csv and create ../output/report.csv

python3 -u ~/insight_consumer_complaint_reporting/src/consumer_complaints.py > consumer_complaints.py.log 
