#! /usr/bin python3
# consumer_complaints.py - reads input/complaints.csv file from input dir and creates a report written to output/report.csv

import csv

# data file paths
indata = 'input/complaints_sm.csv'
outdata = 'output/report.csv'

# input datafile very large so use csv module with generator to read input data one line at a time

def read_big_csv(file_path):
    """Designed to read large csv files efficiently with low overhead using csv module with generator.
    Assumes 1st row of csv contain field names."""

    with open(file_path, 'rU') as data:
        reader = csv.DictReader(data)
        for row in reader:
            yield row


    if __name__ == "__main__":
        for idx, row in enumerate(read_big_csv(indata)):
            if idx > 10: break
            print("Number of rows read_big_csv() read in: ", rows)
            

