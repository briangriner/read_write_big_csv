#! /usr/bin python3
# consumer_complaints.py - reads input/complaints.csv file from input dir and creates a report written to output/report.csv

import csv
from collections import Counter

# data file paths
indata = '../input/complaints_11.csv'
outdata = '../output/report.csv'

class ReadBigCSV(object):
    def __init__(self, path):
        self.path  = path
        self._length = None
        self._counter = None

    
    def __iter__(self):
        self._length = 0
        self._counter_p = Counter()
        self._counter_d = Counter()
        with open(self.path, 'r') as data:
            reader = csv.DictReader(data)
            for row in reader:
                # save stats
                self._length += 1
                self._counter_p[row['Product']] += 1
                self._counter_d[row['Date received']] += 1
                yield row


    def __len__(self):
        if self._length is None:
            for row in self:
                continue
            return self._length


    @property
    def counter_p(self):
        if self._counter_p is None:
            for row in self:
                continue
        return self._counter_p


    @property
    def products(self):
        return self.counter_p.keys()


    @property
    def counter_d(self):
        if self._counter_d is None:
            for row in self:
                continue
        return self._counter_d


    @property
    def dates(self):
        return self.counter_d.keys()


    def reset(self):
        """Used if break during read"""
        self._length = None
        self._counter_p = None
        self._counter_d = None


if __name__ == "__main__":
    reader = ReadBigCSV(indata)
    print("%i total complaints with  %i products and %i dates" % (len(reader), len(reader.products), len(reader.dates)))
    for i, row in enumerate(reader):
        print(i, row['Product'], row['Date received'])


