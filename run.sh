#!/bin/bash
# make.sh - run consumer_complaints.py to read ../input/complaints.csv and create ../output/report.csv

python3 -u ~/read_write_big_csv/src/consumer_complaints.py > consumer_complaints.py.log 
