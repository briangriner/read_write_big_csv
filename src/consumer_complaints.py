#! /usr/bin/python3
"""consumer_complaints.py - reads large csv, maps fields to named tuples, uses generator with reduce to compute total, 
uses reducer func with default dict to create list of dicts.L
PATHS ASSUME REPO IN HOME DIR. IF NOT IN HOME ADJUST PATHS IN LINES 12, 13.""" 

import csv, itertools, os
from pathlib import Path
from collections import Counter, namedtuple, defaultdict
from functools import reduce

# data file paths - CHECK PATHS
indata =  'read_write_big_csv-master/input/complaints_11.csv'
outdata = 'read_write_big_csv-master/output/report.csv'

# pathlib .joinpath()
home_path = Path.home()
input_path = home_path.joinpath(indata)
output_path = home_path.joinpath(outdata)

# namedtuple instead of dict
fields = ("Date_received", "Product", "Sub_product", "Issue", "Sub_issue", "Consumer_complaint_narrative", "Company_public_response", "Company", "State", "ZIP_code", "Tags", "Consumer_consent_provided", "Submitted_via", "Date_sent_to_company", "Company_response_to_consumer", "Timely_response", "Consumer_disputed", "Complaint_ID")
#print(fields)

Complaints = namedtuple("Complaints", fields)
#print(Complaints._fields)

# use defaultdict to reduce fields
#cols_dd = defaultdict(list)

# input datafile very large so use csv module with generator to read input data one line at a time
def read_big_csv(file_path):
    """Designed to read large csv files efficiently with low overhead using csv module with generator.
    Assumes 1st row of csv contain field names."""
    with open(file_path, 'r') as data:
        data.readline()
        reader = csv.reader(data)
        #cols = (cols_dd['Product'], cols_dd['Date_received'], cols_dd['Company']) 
        for row in map(Complaints._make, reader):
            yield row[1], row[0], row[7]  #from (row[i] for i in cols)


def reducer(acc, val):
    acc[val[0], val[1][0:4]].append(val[2])
    return acc


# use reduce to calculate totals and subtotals
total_complaints = reduce(lambda acc, val: acc + 1, read_big_csv(input_path), 0)
prod_date = reduce(reducer, read_big_csv(input_path), defaultdict(list))
print(type(prod_date))


if __name__ == "__main__":
    print("Program starting")
    for row in read_big_csv(input_path):
        prod_date


print("prod_date")
print("-"*72)
print(prod_date)

wdata = open(output_path, "a", newline="")
writer = csv.writer(wdata, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
names = ["product", "year", "total number of complaints", "total number of companies"] 
writer.writerow(names)
for prod, dt in prod_date.items():
    row = [str(prod[0]), prod[1], len(dt), len(set(dt))]
    print(row)
    writer.writerow(row)  
  

print("-"*72)
print("Total complaints in file: ", total_complaints)
print("Program finished")

