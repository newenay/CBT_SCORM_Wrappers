#!/usr/bin/env python3

import csv
import json
import sys

# https://www.geeksforgeeks.org/convert-csv-to-json-using-python/
# https://www.geeksforgeeks.org/json-dumps-in-python/

def make_json(csvFilePath, jsonFilePath):

    data = {}

    # bad characters show up as '\ufffd'
    with open(csvFilePath, encoding='latin1') as csv_f:
        csvReader = csv.DictReader(csv_f)
        for rows in csvReader:
            # column name to use as a key
            key = rows['id']
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as json_f:
        # const slideInfo = [data]
        json_f.write(json.dumps(data, indent="\t"))
        #json_f.write(json.dumps(data, indent=4))

csvFilePath = "{}_info.csv".format(sys.argv[1])
jsonFilePath = "{}_info.json".format(sys.argv[1])

make_json(csvFilePath, jsonFilePath)

"""
( ) --> \u00a0 = blank space
(-) --> \u0096 = &dash; or &ndash; (long dash)
(é) --> \u00e9 = &eacute;

(‘) --> &lsquo;
(’) --> \u0092 = &rsquo;
(“) --> &ldquo;
(”) --> &rdquo;
(°) --> &deg;
(…) --> &hellip;
(§) --> &sect;

"""