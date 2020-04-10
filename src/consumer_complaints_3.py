#! /usr/bin python3
# consumer_complaints.py - reads input/complaints.csv file from input dir and creates a report written to output/report.csv

import csv
from collections import namedtuple

# data file paths
indata = '../input/complaints_11.csv'
outdata = '../output/report.csv'

# namedtuple instead of dict
fields = ("Date_received", "Product", "Sub_product", "Issue", "Sub_issue", "Consumer_complaint_narrative", "Company_public_response", "Company", "State", "ZIP_code", "Tags", "Consumer_consent_provided", "Submitted_via", "Date_sent_to_company", "Company_response_to_consumer", "Timely_response", "Consumer_disputed", "Complaint_ID")

complaints = namedtuple("complaints", fields)

#print(complaints)
print(type(complaints))
print(complaints._fields)
print(complaints.__doc__)

# input datafile very large so use csv module with generator to read input data one line at a time

def read_big_csv(file_path):
    """Designed to read large csv files efficiently with low overhead using csv module with generator.
    Assumes 1st row of csv contain field names."""
    with open(file_path, 'r') as data:
        data.readline()
        reader = csv.reader(data)       
        for row in map(complaints._make, reader):
            yield row


if __name__ == "__main__":
    print("Program starting")
    wdata =  open(outdata, 'a')
    writer = csv.writer(wdata)
    for row in read_big_csv(indata):
        prod_date_company = (row[1], row[0], row[7])
        print(prod_date_company)
        writer.writerow(prod_date_company) 
              

print("Program finished")

